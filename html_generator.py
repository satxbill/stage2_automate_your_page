##--------------------------------------------------------------
#
# Stage 2 - html_generator.py
#
# Generates HTML for part of the HMTL notes page I've 
# created during this class
#
##--------------------------------------------------------------
#
# Structured Lists used in my code:
#
# topicList -> contains 1 to many elements. Each element contains a Title sting
# and a description string - also referred to as a 'list of concepts'
#
# lesson -> contains 3 elements.  a lesson id string,  title string and a 
#           topicList element
#
# course -> contains a title at course[0], an HTML page title at course[1]
# and 1 to many lesson list elements at course[2] to course[last]
##--------------------------------------------------------------
#
# Course Topic data goes here go here.  Topic list variables are
# named to align with the course lesson they belong to.
#
# Only data for the first lesson has been entered here.  All
# that remains to generate the full HTML page of my notes is
# to populate the remaining 'topicList_Lessonx_x' lists.
#
##--------------------------------------------------------------
topicList_Lesson1_1 = [
# topic
["Web Structure", '''
The basic high level elements of "The Web" are user's computers running browsers, the Internet, and Servers'''],
# next topic
["HTML", '''
HTML stands for <em>HyperText Markup Language</em>. HTML documents make up the 
majority of the content on the web. HTML documents contain <em>text content</em> 
which describes "what you see" and <em>markup</em> which describes "how it looks".'''],
#next topic
["Tags and Elements", '''
HTML documents are comprised of <em>HTML Elements</em>. HTML Elements are defined using HTML 
Tags. Tags typically have begin and end components, with <em>void</em> type tags being an exception 
only having a single component. An example of a void tag is the "br" tag.
<br><br>
Some tags have content, some have content and attributes. Some tags are <em>inline</em>, 
menaing they work 'inline' with other HTML elements. Some tags are <em>block</em> - which 
for now means they create an invisible block in the HTML document that can have attributes 
which we'll learn about later.'''],
# topic
["Stupid Computers!!",'''
Computers only do what we tell them to do (at least for now)...
''']
#end of topic list
]
##
# The remaining lessons' topics would be entered here.  They are stubbed out
# and HTML will be generated for all lessons.
##
topicList_Lesson1_2 = [["Title in 1.2","Description in 1.2"]]
topicList_Lesson1_3 = [["Title in 1.3","Description in 1.3"]]
topicList_Lesson2_1 = [["Title in 2.1","Description in 2.1"]]
topicList_Lesson2_2 = [["Title in 2.2","Description in 2.2"]]
topicList_Lesson2_3 = [["Title in 2.3","Description in 2.3"]]
topicList_Lesson2_4 = [["Title in 2.4","Description in 2.4"]]
topicList_Lesson2_5 = [["Title in 2.5","Description in 2.5"]]
topicList_Lesson2_6 = [["Title in 2.6","Description in 2.6"]]
topicList_Lesson2_7 = [["Title in 2.7","Description in 2.7"]]


##--------------------------------------------------------------
# the Lesson lists for Introduction to Programming
#
# lesson lists contain 3 elements:
#     [0] -> the lesson id - this is used in my HTML by the nav menu
#     [1] -> the lesson title - used in the HTML to display the lesson title
#     [2] -> a list consisting of lesson topics (see above for that list structure)
#
# Only the first 3 lessons have valid data, the remaining lessons are stubbed out.
##--------------------------------------------------------------
lesson1_1 = ["lesson1-1", "1.1: The Basics of Web and HTML", topicList_Lesson1_1]
lesson1_2 = ["lesson1-2", "1.2: Creating a Structured Document with HTML", topicList_Lesson1_2]
lesson1_3 = ["lesson1-2", "1.3: Adding CSS Style and HTML Structure", topicList_Lesson1_3]
lesson2_1 = ["lesson2-1", "2.1: title", topicList_Lesson2_1]
lesson2_2 = ["lesson2-2", "2.2: title", topicList_Lesson2_2]
lesson2_3 = ["lesson2-3", "2.3: title", topicList_Lesson2_3]
lesson2_4 = ["lesson2-4", "2.4: title", topicList_Lesson2_4]
lesson2_5 = ["lesson2-5", "2.5: title", topicList_Lesson2_5]
lesson2_6 = ["lesson2-6", "2.6: title", topicList_Lesson2_6]
lesson2_7 = ["lesson2-7", "2.7: title", topicList_Lesson2_7]

##--------------------------------------------------------------
# course list for Introduction to Programming
#
# course lists contain the following elements:
#     [0] -> string containing the course title
#     [1] -> string containing a page title for the HTML <head> block
#     [2+] -> as many lessons as are in the course.  Lesson lists are defined above
##--------------------------------------------------------------
course_introToProgramming = ["Introduction to Programming",
                             "Stage2 HTML v2.0",
                              lesson1_1,
                              lesson1_2,
                              lesson1_3,
                              lesson2_1,
                              lesson2_2,
                              lesson2_3,
                              lesson2_4,
                              lesson2_5,
                              lesson2_6,
                              lesson2_7]
##--------------------------------------------------------------
# end of the data used by this program.
##--------------------------------------------------------------

##--------------------------------------------------------------
# Algorithm
#
# the main routine, generate_html_for_course, does the following:
#
# 1 - generates the page header HTML, including the <head> section,
#     <body> tag and the <div> tag that creates the container for
#     the remaining page elements
# 2 - parses through the lessons in the course and generates 
#     each lesson container and all of the topic containers 
#     within each lesson container
# 3 - generats the 'footer' information for the HTML page including
#     the </body> and </html> tags. Also the </div> tag to close
#     the main container started in step 1.
#
# The data structure used facilitates the structure of the code
# by providing a logically grouped representation of the data.
##--------------------------------------------------------------

##--------------------------------------------------------------
# Functions used.  Descriptions of each are provided in the comment
# block immediately preceding each function.
##--------------------------------------------------------------

##--------------------------------------------------------------
# generate_main_title_block - creates a 'main title block' of html
#
# this block of html appears many times in my html code so I 
# created this simple procedure to generate that code
#
# inputs - block id string, title string
# outputs - 3 lines of an html <div> block
##--------------------------------------------------------------
def generate_main_title_block(block_id, title):
    html_1 ='''
            <div class="main_title">
                <h2 id="''' + block_id +'">' + title + '</h2>'  
    html_2 = '''
            </div>'''

    return html_1 + html_2
##--------------------------------------------------------------
# generate_HTML_page_header will create the page header and main_page
# container
##--------------------------------------------------------------
def generate_HTML_page_header(page_title, course_title):
    html_1 = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>''' + page_title + "</title>"

    html_2 = '''
    <link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>
    <div class="main_page"> <!-- this is the main box for the page -->
    <!-- 
        Page header
    -->'''

    html_3 = generate_main_title_block("top_of_page", course_title) 

    generated_HTML = html_1 + html_2 + html_3
    return generated_HTML

##--------------------------------------------------------------
# generate_HTML_page_footer will create the html to end the page
#
# this is static - no inputs.  created function for consistency
# and readability of the main code.
##--------------------------------------------------------------
def generate_HTML_page_footer():
    generated_HTML = '''
<!--
    page footer
-->
    </div>  <!-- end of main box for the page -->
</body>

</html>'''

    return generated_HTML

##--------------------------------------------------------------
# generate_standard_content_panel will generatet the standard content panel 
# for my html page
#
# inputs = concept_title string and concept_description string
##--------------------------------------------------------------
def generate_standard_content_panel(concept_title, concept_description):
    html_text_1 = '''
            <div class="standard_content panel"> <!-- start of panel -->
                <h2 class="standard_content_title"> 
        ''' + "            " + concept_title
    html_text_2 = '''
                </h2>
                <p>
    ''' + "                " + concept_description
    html_text_3 = '''
                </p>
            </div>'''
    generated_HTML = html_text_1 + html_text_2 + html_text_3
    return generated_HTML

##--------------------------------------------------------------
# generate_navigation_menu will generate the html for the menu
#
# Note - this will be implemented later...
##--------------------------------------------------------------
def generate_navigation_menu(menu_list):
	generated_HTML = ''
	return generated_HTML

##--------------------------------------------------------------
# generate_lesson_header_HTML generates the HTML at the start
# of each block of lesson topics
#
# inputs - lesson
# outputs - html
##--------------------------------------------------------------
def generate_lesson_header_HTML(lesson):
	lessonID = lesson[0]
	lessonTitle = lesson[1]
	html_1 = '''
<!--
    Notes from ''' + lessonID
        html_2 = '''
-->'''
	html_3 = generate_main_title_block(lessonID, lessonTitle)
	html_4 = '''
	        <div class="main_lesson centered_row"> <!-- ''' + lessonID + " -->"
	generated_HTML = html_1 + html_2 + html_3 + html_4
	return generated_HTML

##--------------------------------------------------------------
# generate_lesson_footer_HTML generates the HTML at the end of 
# each lesson section's HTML.  
##--------------------------------------------------------------
def generate_lesson_footer_HTML(lesson):
	lessonID = lesson[0]
	html_1 ='''
	        </div> <!-- end of ''' + lessonID + "-->" 
	return html_1 

##--------------------------------------------------------------
# generate_HTML_for_lesson_topics will create HTML for all topics
# in a given lesson.  HTML for concepts is the same regardless
# of which course or lesson
#
# input - list of concepts 
# output - html to build a standard content block for each
#          concept
##--------------------------------------------------------------
def generate_HTML_for_lesson_topics(list_of_concepts):
    # write code here that generates the appropriate HTML
    # for a list of concepts.
    output_html = ""
    for concept_element in list_of_concepts:
        title = concept_element[0]
        description = concept_element[1]
        output_html = output_html + generate_standard_content_panel(title, description)
    return output_html

##--------------------------------------------------------------
#  main procedure code starts here
##--------------------------------------------------------------

##--------------------------------------------------------------
# code to generate the HTML for all of the lessons in the course
# 
# this is the main procedure code
#
# input -> structured list containing notes for one course
#
# course lists contain the following elements:
#     [0] -> string containing the course title
#     [1] -> string containing a page title for the HTML <head> block
#     [2+] -> lists for each lesson in the course.  
#          
##--------------------------------------------------------------
def generate_html_for_course(course):
	title = course[0]
	html_page_title = course[1]
	generated_HTML = generate_HTML_page_header(html_page_title, title)
	#
	# start from index position 2 to get the first lesson in the course
	#
	i = 2
	while i < len(course):
		current_lesson = course[i]
		current_topic_list = current_lesson[2]
		generated_HTML = generated_HTML + generate_lesson_header_HTML(current_lesson)
		generated_HTML = generated_HTML + generate_HTML_for_lesson_topics(current_topic_list)
		generated_HTML = generated_HTML + generate_lesson_footer_HTML(current_lesson)
		i += 1
	generated_HTML = generated_HTML + generate_HTML_page_footer()
	return generated_HTML


##
# run the code...
##
print generate_html_for_course(course_introToProgramming)



