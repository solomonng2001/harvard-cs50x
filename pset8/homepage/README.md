[Homepage](https://cs50.harvard.edu/x/2021/psets/8/homepage/#homepage)
======================================================================

Build a simple homepage using HTML, CSS, and JavaScript.

[Background](https://cs50.harvard.edu/x/2021/psets/8/homepage/#background)
--------------------------------------------------------------------------

The internet has enabled incredible things: we can use a search engine to research anything imaginable, communicate with friends and family members around the globe, play games, take courses, and so much more. But it turns out that nearly all pages we may visit are built on three core languages, each of which serves a slightly different purpose:

1.  HTML, or *HyperText Markup Language*, which is used to describe the content of websites;
2.  CSS, *Cascading Style Sheets*, which is used to describe the aesthetics of websites; and
3.  JavaScript, which is used to make websites interactive and dynamic.

Create a simple homepage that introduces yourself, your favorite hobby or extracurricular, or anything else of interest to you.

[Specification](https://cs50.harvard.edu/x/2021/psets/8/homepage/#specification)
--------------------------------------------------------------------------------

Implement in your `homepage` directory a website that must:

-   Contain at least four different `.html` pages, at least one of which is `index.html`(the main page of your website), and it should be possible to get from any page on your website to any other page by following one or more hyperlinks.
-   Use at least ten (10) distinct HTML tags besides `<html>`, `<head>`, `<body>`, and `<title>`. Using some tag (e.g., `<p>`) multiple times still counts as just one (1) of those ten!
-   Integrate one or more features from Bootstrap into your site. Bootstrap is a popular library (that comes with lots of CSS classes and more) via which you can beautify your site. See [Bootstrap's documentation](https://getbootstrap.com/docs/4.5/) to get started. In particular, you might find some of [Bootstrap's components](https://getbootstrap.com/docs/4.5/components/) of interest. To add Bootstrap to your site, it suffices to include

    ```
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>

    ```

    in your pages' `<head>`, below which you can also include

    ```
    <link href="styles.css" rel="stylesheet">

    ```

    to link your own CSS.

-   Have at least one stylesheet file of your own creation, `styles.css`, which uses at least five (5) different CSS selectors (e.g. tag (`example`), class (`.example`), or ID (`#example`)), and within which you use a total of at least five (5) different CSS properties, such as `font-size`, or `margin`; and
-   Integrate one or more features of JavaScript into your site to make your site more interactive. For example, you can use JavaScript to add alerts, to have an effect at a recurring interval, or to add interactivity to buttons, dropdowns, or forms. Feel free to be creative!
-   Ensure that your site looks nice on browsers both on mobile devices as well as laptops and desktops.

<sub>*Assignment description taken from https://cs50.harvard.edu/x/2021/*</sub>
