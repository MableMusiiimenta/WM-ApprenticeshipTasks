today we prepared your local WordPress installation so that you can 
write your own plugin directly in your normal project directory.

WordPress can already see:

     Bobo Training

but at the moment the plugin does not actually do anything.

Your task today is to change that.

The goal is not to build a large plugin.

The goal is to understand this flow:

     WordPress encounters something
         ↓
     WordPress calls your function
         ↓
     WordPress gives information to the function
         ↓
     your function processes it
         ↓
     your function returns a result
         ↓
     WordPress puts that result into the page

This is also an exercise in:

     functions
     parameters
     variables
     scope
     return values

### 1. Document the plan first

Create:

     week-4/friday/first-wordpress-plugin.md

Write:

     Plugin purpose:

     What should the user put into a WordPress page?

     What should appear on the frontend?

     Which function will WordPress call?

     What information does the function need?

     What should the function return?

For today we are going to create a shortcode.

A shortcode is something that can be put into WordPress content, for 
example:

     [bobo_project]

WordPress can recognize that shortcode and call a PHP function 
registered by your plugin.

### 2. Make the smallest working shortcode

In your existing Bobo Training plugin, register:

     [bobo_project]

WordPress provides:

     add_shortcode()

The basic pattern is:

     add_shortcode(
         'shortcode_name',
         'function_name'
     );

Create a function called something like:

     bobo_project_shortcode()

For the first version, do not use any parameters yet.

It should simply return some HTML.

For example, conceptually:

     <p>This content came from the Bobo Training plugin.</p>

Important:

The shortcode function should:

     return the result

not:

     echo the result

Add:

     [bobo_project]

to one of your WordPress pages and view the page on the frontend.

Verify that your plugin-generated content appears.

### 3. Explain what just happened

Before adding anything else, document the flow.

Start with:

     WordPress page contains:
     [bobo_project]

Then explain:

     How does WordPress know which function to call?
     By checking the function add_shortcode, the shortcode it finds in the function determines its corresponding function

     Who calls bobo_project_shortcode()?
     the shortcode bobo_project

     Does the function run when you edit the page or when WordPress 
renders the frontend page?
It runs when WordPress renders the frontend page

     What does the function return?
It returns $content

     Where does the returned HTML end up?
     It ends up on the frontend page


### 4. Add one shortcode attribute

Now make the shortcode accept some information.

We want to be able to write:

     [bobo_project title="WordPress Training"]

The function registered as the shortcode callback receives shortcode 
attributes through a parameter.

The general shape can be:

     function bobo_project_shortcode( $atts ) {
         ...
     }

Here:

     $atts

is a parameter.

WordPress supplies its value when it calls your function.

This is the same concept we discussed with functions in Python:

     function definition
         → declares what information the function can receive

     function call
         → supplies the actual information

WordPress provides a helper called:

     shortcode_atts()

Use it to define a default value for `title`.

Conceptually:

     title defaults to "Project"

If the user writes:

     [bobo_project]

the default should be used.

If the user writes:

     [bobo_project title="Local WordPress"]

the supplied value should be used.

### 5. Stop and trace the variables

Before continuing, document this exact flow:

     [bobo_project title="Local WordPress"]
                       ↓
                 WordPress
                       ↓
             callback function
                       ↓
                    $atts
                       ↓
                   $title
                       ↓
                 returned HTML

Answer:

     Who creates the original value "Local WordPress"?
     The user

     Who passes it to the PHP function?
the shortcode bobo_project

     Which parameter receives it?
     $atts

     Where is $atts available?
     It is in the callback function bobo_project_shortcode

     If another function exists in the plugin, can that function 
automatically access $atts?
No

     Why or why not?
     Because $atts is defined in bobo_project_shortcode function and can't be accessed out of it


### 6. Build a small Project Card

Extend the shortcode so we can write something similar to:

     [bobo_project
         title="Local WordPress"
         status="In progress"
     ]

You do not need to put it on several lines in WordPress; that is only 
shown here for readability.

Support these attributes:

     title
     status

Use defaults if they are missing.

For example:

     title:
     Project

     status:
     Learning

The resulting frontend could conceptually contain:

     Local WordPress

     Status: In progress

Use simple HTML.

Do not spend much time styling it.

### 7. Safe output

The values in shortcode attributes ultimately come from content a user 
can edit.

Before putting plain text into generated HTML, WordPress provides:

     esc_html()

For example:

     esc_html( $title )

Use `esc_html()` for the visible title and status.

Think back to our validation discussion:

     input
         ↓
     application
         ↓
     output

We do not simply trust arbitrary values when putting them into HTML.

For today, you do not need to study the complete WordPress security API.

Just understand why output originating from a variable should be handled 
deliberately.

### 8. Test different cases

Test:

     [bobo_project]

Expected:

     defaults are displayed


     [bobo_project title="WordPress Training"]

Expected:

     custom title
     default status


     [bobo_project title="WordPress Training" status="Complete"]

Expected:

     both custom values


Also try changing the shortcode values and refreshing the frontend.

Because your plugin directory is mounted into Docker, you should not 
need to copy your PHP file into the container again.

Save your code and reload the website.

### 9. Function contract

Add this to your documentation:

     Function:
     bobo_project_shortcode()

     Responsibility: 

     Parameters: $atts, $content

     Who supplies the parameter:

     Local variables:

     Return value:

     Who uses the return value:

Then explain the difference between:

     $atts

and:

     $title

Why do we receive `$atts`, but then create a `$title` variable?

### 10. Compare with Flask

Write a short comparison.

In Flask you had approximately:

     browser request
         ↓
     route function
         ↓
     variables / database
         ↓
     template
         ↓
     HTML response

Today you have:

     WordPress page content
         ↓
     shortcode encountered
         ↓
     shortcode callback function
         ↓
     attributes
         ↓
     returned HTML
         ↓
     WordPress inserts it into the page

What is similar?

What is different?

### 11. Code readability

Before finishing, review your PHP.

Check:

     meaningful function name

     meaningful variable names

     consistent indentation

     consistent spaces

     no unnecessary code

     function has one clear responsibility

Don't worry about memorizing WordPress functions such as 
`add_shortcode()` or `shortcode_atts()`.

It is normal to look framework functions up.

I am more interested in whether you understand:

     what data goes into your function
     what happens inside it
     what comes back out
     who uses the result

### 12. Optional challenge

Only do this after everything above works.

Add another optional attribute:

     url

For example:

     [bobo_project
         title="My Website"
         status="Complete"
         url="https://example.com"
     ]

If a URL exists, add a link to the returned HTML.

WordPress provides:

     esc_url()

for safely outputting URLs.

If no URL is supplied, the card should still work without a link.

Think carefully about the control flow rather than copying several 
conditions until something happens.

### End-of-day update

Please send:

Done: 
Documented first-wordpress-plugin.md
Made a working shortcode
Explained what just happened
Added shortcode attributes
Built a small Project Card
Tested different cases

Learned:
I learnt that the different html contents to be returned are separated by space and fullstop, the semi-colon only comes at the end.
I learnt that WordPress checks user input before defaulting to plugin values
And every pHp statement ends with a semicolon


Blocked:

Questions:

Documentation used: Wordpress documentation, PHP documentation

AI used: 

Commit hash, if you put the plugin into Git:

What does add_shortcode() connect together?
It connects wordpress to the shortcode bobo_project

Who calls bobo_project_shortcode()?
the shortcode bobo_project

What is passed into $atts?
attributes for what the user can change

What is the difference between $atts and $title?
$atts is a parameter of the function and $title is one of the $atts

Where is $title available?
It is in the variable $atts

Why does the shortcode function return HTML rather than echo it?
I think it's because return wraps up the function so that nothing further runs after it

What happens to the returned HTML?
It gets displayed on the frontend page

Why did we use esc_html()?
To validate and strip the text of invalid characters before output

What happens if the shortcode does not provide a title?
The page defaults to the title supplied by the plugin, in this case, Project

One thing about function parameters that is clearer now:
They are variables that are awaiting value assignment

One thing about WordPress application flow that is clearer now:
That wordpress checks the plugin for add_shortcode function which then goes through to run a shortcode on the frontpage

One thing I still do not understand:
esc_html, esc_url
