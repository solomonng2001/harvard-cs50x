#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

//Defining data units in JPEG
typedef uint8_t BYTE;
#define BLOCK 512

int main(int argc, char *argv[])
{
    //Prompt if not just one command line argument
    if (argc != 2)
    {
        printf("Usage: ./recover inputfile\n");
        return 1;
    }

    //Open forensic file and prompt if unable to open
    FILE *inputfile = fopen(argv[1], "r");
    if (inputfile == NULL)
    {
        printf("Unable to open %s.\n", argv[1]);
        return 1;
    }

    //Setting of variables & arrays used in following while loop
    BYTE buffer[BLOCK];
    int jpegcount = 0;
    char *filename = malloc(8);
    FILE *outputjpeg = NULL;

    //Continuous loop so long as ther are blocks left to be read in forensic file
    while (fread(buffer, sizeof(BYTE), BLOCK, inputfile) == BLOCK)
    {
        //Check if start of new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            
            //Check if first JPEG file
            if (jpegcount == 0)
            {
                //Create first new JPEG file
                sprintf(filename, "%03i.jpg", jpegcount);
                outputjpeg = fopen(filename, "w");
                
                //Prompt if unable to create first new JPEG file
                if (outputjpeg == NULL)
                {
                    fclose(inputfile);
                    printf("Unable to create output JPEG.\n");
                    return 1;
                }
                
                //Copy over to first new JPEG file
                fwrite(buffer, sizeof(BYTE), BLOCK, outputjpeg);
                jpegcount++;
            }
            //Not first JPEG & start of new JPEG
            else
            {
                //Close previous JPEG file
                fclose(outputjpeg);
                
                //Open new JPEG file
                sprintf(filename, "%03i.jpg", jpegcount);
                outputjpeg = fopen(filename, "w");
                
                //Prompt if unable to create new JPEG file
                if (outputjpeg == NULL)
                {
                    fclose(inputfile);
                    printf("Unable to create output JPEG.\n");
                    return 1;
                }
                
                //Copy over to new JPEG file
                fwrite(buffer, sizeof(BYTE), BLOCK, outputjpeg);
                jpegcount++;
            }
        }
        //Not start of JPEG and first JPEG already found
        else if (jpegcount > 0)
        {
            //Coninue to copy over to current JPEG folder
            fwrite(buffer, sizeof(BYTE), BLOCK, outputjpeg);
        }
    }

    //Free memory used and close remaining files
    free(filename);
    fclose(inputfile);
    fclose(outputjpeg);
    return 0;
}