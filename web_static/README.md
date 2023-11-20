### About Project 

- all files of project (*.css *.html images ) are in directory AirBnB_clone/web_static
- goal of project to learn HTML && css 
- Html : describes the structure of a Web page
- css: specifying how Web page is  presented to users

### Background Context
Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!
Before developing a big and complex web application, we will build the front end step-by-step.
The first step is to “design” / “sketch” / “prototype” each element:

- Create simple HTML static pages
- Style guide
- Fake contents
- No Javascript
- No data loaded from anything
- 
During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

Before starting, please fork or clone the repository AirBnB_clone from your partner if you were not the owner of the previous project.

### execution 

- each file 0-index.html to 8-index.html has its own css files (folder styles)
- to build the final web page version (8-index.html) , we procede by adding some style in each revision of xx.index (xx: 0-->8)

launching 8-index.html on: 
- Microsoft Edge for Business - Version 119.0.2151.72 (Version officielle) (64 bits)

![logo project Hbnb.](https://github.com/dev-tch/AirBnB_clone/blob/main/pictures/test_web_page.PNG)

### Requirements 

Your code should be W3C compliant and validate with W3C-Validator
Exeception accepted : 4-index.html won’t be W3C valid, don’t worry, it’s temporary


Test1 
 ```
$ python w3c_validator.py  /d/_AirBnb/AirBnB_clone/web_static/*.html
'D:/_AirBnb/AirBnB_clone/web_static/4-index.html' => Section lacks heading. Consider using “h2”-“h6” elements to add ident
ifying headings to all sections, or else use a “div” element instead for any cases where no heading is needed.
'D:/_AirBnb/AirBnB_clone/web_static/0-index.html' => OK
'D:/_AirBnb/AirBnB_clone/web_static/1-index.html' => OK
'D:/_AirBnb/AirBnB_clone/web_static/2-index.html' => OK
'D:/_AirBnb/AirBnB_clone/web_static/3-index.html' => OK
'D:/_AirBnb/AirBnB_clone/web_static/5-index.html' => OK
'D:/_AirBnb/AirBnB_clone/web_static/6-index.html' => OK
'D:/_AirBnb/AirBnB_clone/web_static/7-index.html' => OK
'D:/_AirBnb/AirBnB_clone/web_static/8-index.html' => OK
 ```

Test2

 ```
$ python w3c_validator.py  /d/_AirBnb/AirBnB_clone/web_static/styles/*.css
'D:/_AirBnb/AirBnB_clone/web_static/styles/2-common.css' => OK
'D:/_AirBnb/AirBnB_clone/web_static/styles/2-footer.css' => OK
'D:/_AirBnb/AirBnB_clone/web_static/styles/2-header.css' => OK
'D:/_AirBnb/AirBnB_clone/web_static/styles/3-common.css' => OK
'D:/_AirBnb/AirBnB_clone/web_static/styles/3-footer.css' => OK
'D:/_AirBnb/AirBnB_clone/web_static/styles/3-header.css' => OK
'D:/_AirBnb/AirBnB_clone/web_static/styles/4-common.css' => OK
'D:/_AirBnb/AirBnB_clone/web_static/styles/4-filters.css' => OK
'D:/_AirBnb/AirBnB_clone/web_static/styles/5-filters.css' => OK
'D:/_AirBnb/AirBnB_clone/web_static/styles/6-filters.css' => OK
'D:/_AirBnb/AirBnB_clone/web_static/styles/7-places.css' => OK
'D:/_AirBnb/AirBnB_clone/web_static/styles/8-places.css' => OK
 ```


