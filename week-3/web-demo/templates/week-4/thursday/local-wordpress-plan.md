today we looked at how your local WordPress site is put together and how content in WordPress admin becomes the frontend website.

For your independent work, I would like you to turn the local installation into a small but coherent website.

The goal is not to create a beautiful finished design.

The goal is to practise:

frontend → identify owner → CMS change → predict effect → verify effect
and to understand which parts of WordPress are responsible for different parts of the website.

Please work only in your local WordPress installation.

Plan the site before editing

Create:

week-4/thursday/local-wordpress-plan.md
Plan a small personal/developer website with these pages:

Home
Purpose:
Main heading:
Main content:
Important link or button:
Which WordPress area should contain this content?

About
Purpose:
Main heading:
Main content:
Important link or button:
Which WordPress area should contain this content?

Projects
Purpose:
Main heading:
Main content:
Important link or button:
Which WordPress area should contain this content?

Contact
Purpose:
Main heading:
Main content:
Important link or button:
Which WordPress area should contain this content?


Each page should contain at least:

a meaningful title
one heading inside the page content
some paragraph content
Use different Gutenberg blocks where they make sense.

For example:

Heading
Paragraph
Image
Buttons
List
Do not add blocks only because they exist. Use blocks that serve the content.

Build the site navigation

Create or update the main navigation so the user can reach:

Home
About
Projects
Contact
Afterward, test every link from the frontend.

Think about:

Is navigation page content?

Is it part of the theme/template?

Why does changing the navigation affect multiple pages?
Document your answers.

Work with the site-wide template

Use the Site Editor to inspect the parts around the page content.

Identify:

site title
header
navigation
main content area
footer
Make one small site-wide change.

For example:

change the site title
or:

adjust the footer content
Before making the change, write:

What am I changing?

Which WordPress layer owns it?

Which pages do I expect this change to affect?
Then make the change and verify your prediction.

Add one image

Upload one image through the WordPress Media Library and use it on one of your pages.

Add suitable alternative text.

Then think about what we discussed today:

Most page/settings information is persistent database data.

The actual uploaded image is also stored as a file.

Do not worry about the exact WordPress database structure yet.

Just document:

Which part is a file?

Which information about the image do you think WordPress still needs to remember in the database?
6. Create one Post

We discussed the difference between Pages and Posts.

Create one simple blog Post called something like:

What I Learned About WordPress
Write a few sentences about something you learned this week.

Then compare the Post with one of your Pages.

Document:

What is similar?

What is different?

When would you use a Page?

When would you use a Post?
7. Create a CMS ownership map

Add a section to:

local-wordpress-plan.md
For these frontend elements, document where you found their source:

Homepage title
Homepage body text
Site title
Header
Navigation
Footer
Uploaded image
Blog post
Use this format:

Frontend element:
Controlled by:
Where I edit it:
Expected scope of change:
For example:

Frontend element:
Main navigation

Controlled by:
Theme / navigation block

Where I edit it:
Site Editor

Expected scope of change:
Multiple pages because the header is shared
The important question is:

If I see something on the frontend, how do I work out which part of WordPress owns it?

Inspect the WordPress database — read only

This is a small database exercise.

Do not UPDATE, INSERT or DELETE anything directly in the WordPress database.

From the directory containing your compose.yaml, enter the MariaDB container.

Based on our local setup, this should be similar to:

sudo docker compose exec db mariadb -u wordpress -p wordpress
You should be asked for the database password.

Use the password from your local compose.yaml.

Once connected, first run:

SHOW TABLES;
Look for a table named:

wp_posts
Then run:

SELECT ID, post_title, post_type, post_status
FROM wp_posts
ORDER BY ID;
Look for:

your Pages
your new Post
Pay particular attention to:

ID
post_title
post_type
You should be able to see that Pages and Posts are represented as records but have different post_type values.

Then choose one of the pages you created and query it directly by ID:

SELECT ID, post_title, post_type, post_status
FROM wp_posts
WHERE ID = YOUR_ID;
Replace YOUR_ID with the real ID.

Do not change the row.

The objective is only to connect:

WordPress admin
    ↓
persistent database record
    ↓
frontend page
When finished, leave MariaDB with:

exit
If your tables do not begin with wp_, use the actual table names returned by SHOW TABLES;.

Compare WordPress with our Flask application

In your documentation, compare:

Flask application
WordPress
Think about:

Which part receives the browser request?

What stores persistent data?

What renders the frontend?

What corresponds roughly to our templates?

What is different?
You do not need a perfect technical comparison.

The goal is to recognise concepts you already learned in another application.

Final frontend review

Open the site as a normal visitor.

Do not stay inside wp-admin.

Check:

Can I navigate between all pages?

Are headings understandable?

Do links/buttons go where expected?

Does the image have useful alternative text?

Did site-wide changes appear where expected?

Did anything unrelated change accidentally?
Also briefly check the site at a narrow/mobile browser width.

End-of-day update

Please send me:

Done:
Planned wordpress site
Created the pages
Created a Post
Created a CMS ownership map
Inspected the WordPress database

Learned:
Docker can help with its set up
One can write code in WordPress
“Edit site” edits the template parts like header, footer, navigation while “edit page” edits page content
WordPress uses sql
Wordpress is not only used for building sites, it is also for blog posts

Blocked:
I could not search up a plugin outside localhost

Questions:
Why is the post appearing in the site with headers and navigation? I thought it would be simply a post, on its own

Documentation used: 

AI used: None

Which frontend element was easiest to map back to WordPress?
Page title

Which was hardest?
The footer

What is the difference between page content and a template part?
They have different edit buttons/links

Why does changing the header affect several pages?
Because the header is being shared by several pages

What is the difference between a Page and a Post?
A page is part of an element of a website while a post is complete in itself

What did you observe in wp_posts?
I observed that pages and posts are all under post_title but they are differentiated via post type, i.e, page for pages, post for posts and each one has an ID

How could you tell which database row represented a Page and which represented a Post?
By checking the post_type column

What did you learn about the difference between database data and files?
Files, like images are saved as attachment type while database data is saved as post/pages/revision

What did you learn about how WordPress maps CMS content to the frontend?
it combines template parts and page content and displays it as post under wp-posts

One thing about Docker that is clearer now:
It organizes the set up of a project and helps in team collaboration by distributing the same set up

One WordPress concept I still do not understand:
How do forms post?
