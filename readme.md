NOTE:   After cloning the repo RUN the COMMAND in terminal: 'python manage.py runserver' from the current directory






-->         Laying the pipeline | Python Django Tutorials In Hindi #7

    isme humne urls.py file endpoints wala kuch dekha tha




-->         Templates | Python Django Tutorials In Hindi #8

    isme template folder bnaya tha jaha hmara 'manage.py' file hoti usme html files bnayi jaati hain

    uske baad view.py mein templates k liye (from django.shortcuts import render)

    uske baad return function mein 'render(request, <filename.html>)'

    ek isme last argument bhi hota hai (example mein string interpolation k liye use kiya tha) ye dictionary leta hai
            'params3rd ={'name': 'Prasoon', 'place':'India'}'
            'return render(request, 'index.html', params3rd)'     <-- ye sab views.py file mein
      iske baad tempelates mein is dictionary ki keys ko aise use kr sakte hain ({{}})  <-- html file mein
         ex:-  {{name}} is from {{place}}




-->         Creating Homepage of our TextUtils Website | Python Django Tutorials In Hindi #9

    html file ka textarea ka browser (inspect element/ ctrl+shift+i) then edit with html select krna

    button press krne pr action dena (html file m) "<form action='/removepunc' method='get'>" (text filed se data lekar address bar mein)

    html k textarea mein naam diya tha 'name'(html file mein) usko Use krke address bar mein show krana  <-- index.html mein
            ex :- <textarea name='text' style= ''></textarea>

     'request.GET.get('text', 'default')' ka Use krna(view.py file mein) console mein print krane k liye




-->         Django Site: Coding The Backend | Python Django Tutorials In Hindi #10

    just added the checkbox and name
    checkbox enable h toh answer print krana else error(views.py file)
    in backend a for loop to remove delimiter(views.py file)




-->         Django Site: Exercise | Python Django Tutorials In Hindi #11

    solved the exercise
    
    
    

-->         Adding More Features To TextUtils Website | Python Django Tutorials In Hindi #12
    
    add more checkboxes in index.html and then updating the same in views.py for evaluating




-->         Django Exercise 2: Revamping TextUtils | Python Django Tutorials In Hindi #13

    isme 2 or more than 2 checkbox ko enable kiya (if and elif ko if kiya)
    



-->         Adding Bootstrap To Our Django Website | Python Django Tutorials In Hindi #14

    index.html mein bootstrap use kiya tha from website https://getbootstrap.com/
        1. STARTER TEMPLATE uthaya tha   https://getbootstrap.com/docs/4.4/getting-started/introduction/
        2. Class Container bnayi thi                    <div class="container-fluid"></div>
        3. COMPONENTS mein jaa kar
            * NAVBAR uthaya tha    https://getbootstrap.com/docs/4.4/components/navbar/    also us NAVBAR humne <Form tag> use krke 'search' de diya tha aur uske Home and About Us mein anchor tag modify kiya tha   
            * ALert mein se DISMISSABLE ALERTS uthaya tha     https://getbootstrap.com/docs/4.4/components/alerts/
            * FORMS mein jaakr Form Control mein se last mein textarea uthaya tha   https://getbootstrap.com/docs/4.4/components/forms/     also usme SWITCH diye the
            * BUTTONS mein jaa kr Button uthaya tha     https://getbootstrap.com/docs/4.4/components/buttons/
            
            aur FORM tag mein ( <form action='/analyze' method= 'get'>) diya tha         
    
     


-->         Fixing Bugs In Our TextUtils Website | Python Django Tutorials In Hindi #15

    html ki property hoti hai 'newline' ko chop off toh use liye hume <pre></pre> tag Use krte hai

    
    
    
-->         Django CSRF Tokens & Post Request | Python Django Tutorials In Hindi #16

    CSRF - Cross site Request Forgery
    <form> {% csrf_token %} </form> tag (index.html) mein csrf diya tha and (views.py) mein *djtext = request.POST.get('text', 'default')* 'POST' diya tha jisse ki hmara content url mein show na ho isse jab text ki lenghth ho jaati h vo bhi handle ho jaati h kyunki URL ka kuch definite size hota hai




-->         Exercise 2 Solution + Shoutouts | Python Django Tutorials In Hindi #17
    
    
