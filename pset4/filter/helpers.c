#include <math.h>

#include "helpers.h"

int sobel(int Gx, int Gy);
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    //Loop through image array
    for (int i = 0, n = height; i < n; i++)
    {
        for (int j = 0, m = width; j < m; j++)
        {
            //setting each colour channel to average of across each pixel
            BYTE average = round((float)(image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3);
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //Loop through image array
    for (int i = 0, n = height; i < n; i++)
    {
        for (int j = 0, m = width / 2; j < m; j++)
        {
            //Swapping values of mirror pixels
            RGBTRIPLE tmp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = tmp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //Copy of original image array without blur effect
    RGBTRIPLE original[height][width];
    for (int i = 0, n = height; i < n; i++)
    {
        for (int j = 0, m = width; j < m; j++)
        {
            original[i][j] = image[i][j];
        }
    }
    
    //Loop through image array
    for (int i = 0, n = height; i < n; i++)
    {
        for (int j = 0, m = width; j < m; j++)
        {
            //Setting total colour values per colour channel for surrounding 9 pixels of each pixel to 0 & setting count of existent surrounding pixels to 0
            float totalRed = 0;
            float totalBlue = 0;
            float totalGreen = 0;
            float count = 0;
            
            //Looping through surrounding 9 pixels around each pixel
            for (int k = 0; k < 3; k++)
            {
                for (int l = 0; l < 3; l++)
                {
                    //Checking if surrounding pixels are existent and within height and width of image
                    if (i - 1 + k >= 0 && i - 1 + k < height && j - 1 + l >= 0 && j - 1 + l < width)
                    {
                        //Summing total colour values per colour channel and counting number of existent surrounding pixels included in calculation
                        totalRed += original[i - 1 + k][j - 1 + l].rgbtRed;
                        totalGreen += original[i - 1 + k][j - 1 + l].rgbtGreen;
                        totalBlue += original[i - 1 + k][j - 1 + l].rgbtBlue;
                        count++;
                    }
                }
            }
            //Setting new pixel value to average accross surrounding 9 pixels (if existent)
            BYTE Red = image[i][j].rgbtRed = round(totalRed / count);
            BYTE Green = image[i][j].rgbtGreen = round(totalGreen / count);
            BYTE Blue = image[i][j].rgbtBlue = round(totalBlue / count);
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    //Copy of original image array without edges effect
    RGBTRIPLE original[height][width];
    for (int i = 0, n = height; i < n; i++)
    {
        for (int j = 0, m = width; j < m; j++)
        {
            original[i][j] = image[i][j];
        }
    }
    
    //Gx Kernel
    int Gx[3][3] = 
    {
        {-1, 0, 1},
        {-2, 0, 2},
        {-1, 0, 1}
    };
    
    // Gy Kernel
    int Gy[3][3] = 
    {
        {-1, -2, -1},
        {0, 0, 0},
        {1, 2, 1}
    };
    
    //Looping through each pixel in image
    for (int i = 0, n = height; i < n; i++)
    {
        for (int j = 0, m = width; j < m; j++)
        {
            //Sum of Gx values per kernel per channel colour
            float GxRed = 0;
            float GxBlue = 0;
            float GxGreen = 0;
    
            //Sum of Gy values per kernel per channel colour
            float GyRed = 0;
            float GyBlue = 0;
            float GyGreen = 0;
            
            //Looping through each surrounding 9 pixels for each pixel
            for (int k = 0; k < 3; k++)
            {
                for (int l = 0; l < 3; l++)
                {
                    int y = i + k - 1;
                    int x = j + l - 1;

                    if (y >= 0 && y < height && x >= 0 && x < width)
                    {
                        //Summing Kernel values for Gy & Gx respectively
                        GyRed += original[y][x].rgbtRed * Gy[k][l];
                        GyBlue += original[y][x].rgbtBlue * Gy[k][l];
                        GyGreen += original[y][x].rgbtGreen * Gy[k][l];
                        
                        GxRed += original[y][x].rgbtRed * Gx[k][l];
                        GxBlue += original[y][x].rgbtBlue * Gx[k][l];
                        GxGreen += original[y][x].rgbtGreen * Gx[k][l];
                    }
                }
            }
            
            //Assigning result of sobel values to image array
            image[i][j].rgbtRed = sobel(GxRed, GyRed);
            image[i][j].rgbtBlue = sobel(GxBlue, GyBlue);
            image[i][j].rgbtGreen = sobel(GxGreen, GyGreen);
        }
    }
    return;
}

//Abstraction: Sobel function & cap result of Sobel function at 255 & round off result
int sobel(int Gx, int Gy)
{
    float result;
    result = sqrt(Gx * Gx + Gy * Gy);
    if (result > 255)
    {
        result = 255;
    }
    return round(result);
}