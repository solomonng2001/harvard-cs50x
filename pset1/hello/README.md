[Hello](https://cs50.harvard.edu/x/2021/labs/1/hello/#hello)
============================================================

[Getting Started](https://cs50.harvard.edu/x/2021/labs/1/hello/#getting-started)
--------------------------------------------------------------------------------

CS50 IDE is a web-based "integrated development environment" that allows you to program "in the cloud," without installing any software locally. Indeed, CS50 IDE provides you with your very own "workspace" (i.e., storage space) in which you can save your own files and folders (aka directories).

### [Logging In](https://cs50.harvard.edu/x/2021/labs/1/hello/#logging-in)

Head to [ide.cs50.io](https://ide.cs50.io/) and click "Log in" to access your CS50 IDE. Once your IDE loads, you should see that (by default) it's divided into three parts. Toward the top of CS50 IDE is your "text editor", where you'll write all of your programs. Toward the bottom of is a "terminal window" (light blue, by default), a command-line interface (CLI) that allows you to explore your workspace's files and directories, compile code, run programs, and even install new software. And on the left is your "file browser", which shows you all of the files and folders currently in your IDE.

Start by clicking inside your terminal window. You should find that its "prompt" resembles the below.

```
~/ $

```

Click inside of that terminal window and then type

```
mkdir ~/pset1/

```

followed by Enter in order to make a directory (i.e., folder) called `pset1` inside of your home directory. Take care not to overlook the space between `mkdir` and `~/pset1` or any other character for that matter! Keep in mind that `~` always denotes your home directory and `~/pset1` denotes a directory called `pset1`, which is inside of `~`.

Here on out, to execute (i.e., run) a command means to type it into a terminal window and then hit Enter. Commands are "case-sensitive," so be sure not to type in uppercase when you mean lowercase or vice versa.

Now execute

```
cd ~/pset1/

```

to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

```
~/pset1/ $

```

If not, retrace your steps and see if you can determine where you went wrong.

Now execute

```
mkdir ~/pset1/hello

```

to create a new directory called `hello` inside of your `pset1` directory. Then execute

```
cd ~/pset1/hello

```

to move yourself into that directory.

Shall we have you write your first program? From the *File* menu, click *New File*, and save it (as via the *Save* option in the *File* menu) as `hello.c` inside of your `~/pset1/hello`directory. Proceed to write your first program by typing precisely these lines into the file:

```
#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}

```

Notice how CS50 IDE adds "syntax highlighting" (i.e., color) as you type, though CS50 IDE's choice of colors might differ from this problem set's. Those colors aren't actually saved inside of the file itself; they're just added by CS50 IDE to make certain syntax stand out. Had you not saved the file as `hello.c` from the start, CS50 IDE wouldn't know (per the filename's extension) that you're writing C code, in which case those colors would be absent.

[Listing Files](https://cs50.harvard.edu/x/2021/labs/1/hello/#listing-files)
----------------------------------------------------------------------------

Next, in your terminal window, immediately to the right of the prompt (`~/pset1/hello/ $`), execute

```
ls

```

You should see just `hello.c`? That's because you've just listed the files in your `hello`folder. In particular, you *executed* (i.e., ran) a command called `ls`, which is shorthand for "list." (It's such a frequently used command that its authors called it just `ls` to save keystrokes.) Make sense?

[Compiling Programs](https://cs50.harvard.edu/x/2021/labs/1/hello/#compiling-programs)
--------------------------------------------------------------------------------------

Now, before we can execute the `hello.c` program, recall that we must *compile* it with a *compiler*, translating it from *source code* into *machine code* (i.e., zeroes and ones). Execute the command below to do just that:

```
make hello

```

And then execute this one again:

```
ls

```

This time, you should see not only `hello.c` but `hello` listed as well? You've now translated the source code in `hello.c` into machine code in `hello`.

Now execute the program itself by executing the below.

```
./hello

```

Hello, world, indeed!

[Getting User Input](https://cs50.harvard.edu/x/2021/labs/1/hello/#getting-user-input)
--------------------------------------------------------------------------------------

Suffice it to say, no matter how you compile or execute this program, it only ever prints `hello, world`. Let's personalize it a bit, just as we did in class.

Modify this program in such a way that it first prompts the user for their name and then prints `hello, so-and-so`, where `so-and-so` is their actual name.

As before, be sure to compile your program with:

```
make hello

```

And be sure to execute your program, testing it a few times with different inputs, with:

```
./hello
```

<sub>*Assignment description taken from https://cs50.harvard.edu/x/2021/*</sub>
