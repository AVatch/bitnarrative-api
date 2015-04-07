# bitnarrative-api

### Table of Contents

### First Time Setup

```bash
>> virtualenv env
>> source env/bin/activate
>> pip install -r requirements.txt
>> cd bit-narrative-api
>> python manage.py migrate
>> python manage.py createsuperuser
>> python manage.py runserver
```

### Authentication Flow
Currently authentication is token based. That means that upon successful authentication, a response will be returned containing 
a token.


#####Request: POST
```http
/api/v1/api-token-auth/
```
```json
{
  "username":"",
  "password":""
}
```

#####Response
```json
{
  "token":""
}
```

All subsequent requests need to contain the following header:

```
Authorization: Token <token>
```
---
### Endpoints
```
/api/v1/

/api/v1/api-token-auth/

/api/v1/accounts/
/api/v1/accounts/create/
/api/v1/account/<pk>/
/api/v1/account/<pk>/bits/
/api/v1/account/<pk>/communities/
/api/v1/me/

/api/v1/topics/
/api/v1/topics/<pk>/
/api/v1/topics/<pk>/communities/

/api/v1/content/
/api/v1/content/<pk>/
/api/v1/content/<pk>/bits/
/api/v1/content/<pk>/topbits/

/api/v1/bits/
/api/v1/bit/<pk>/
/api/v1/bit/<pk>/accounts/
```
---
#### Accounts
#####Request: GET @auth-required
```http
/api/v1/accounts/
```
#####Response
Paginated result of all accounts. ```next``` and ```previous``` contain ```urls``` to the 
following pages.
```json
{
    "count": 1, 
    "next": null, 
    "previous": null, 
    "results": [
        {
            "id": 1, 
            "last_login": "2015-04-04T04:04:02.226792Z", 
            "username": "avatchinsky", 
            "email": "adrian@adrian.com", 
            "first_name": "Adrian", 
            "last_name": "Vatchinsky", 
            "profile_picture_url": "http://placehold.it/150x150", 
            "is_admin": true, 
            "is_manager": false, 
            "created_at": "2015-04-04T04:03:50.932471Z", 
            "updated_at": "2015-04-07T18:20:20.098732Z"
        }
    ]
}
```
---
#####Request: POST
```http
/api/v1/accounts/create/
```
Required fields: ```username```, ```password```

---
#####Request: GET, PUT, DELETE @auth-required
```http
/api/v1/account/<pk>/
```
Returns (```GET```) an account object and allows update (```PUT```) and deletion (```DELETE```) of account object.
```json
{
    "id": 1, 
    "last_login": "2015-04-04T04:04:02.226792Z", 
    "username": "avatchinsky", 
    "email": "adrian@adrian.com", 
    "first_name": "Adrian", 
    "last_name": "Vatchinsky", 
    "profile_picture_url": "http://placehold.it/150x150", 
    "is_admin": true, 
    "is_manager": false, 
    "created_at": "2015-04-04T04:03:50.932471Z", 
    "updated_at": "2015-04-07T18:20:20.098732Z"
}
```
---
#####Request: GET @auth-required
```http
/api/v1/account/<pk>/bits/
```
Returns a paginated list of bits the authenticated user has interacted with, sorted by most recent
```json
{
    "count": 1, 
    "next": null, 
    "previous": null, 
    "results": [
        {
            "id": 1, 
            "bit": "   When it comes to crowdfunding it is usually  the record breakers that make news ", 
            "content_index": 0, 
            "view_count": 1, 
            "share_count": 0, 
            "up_count": 1, 
            "down_count": 0, 
            "created_at": "2015-04-04T04:31:54.821662Z", 
            "updated_at": "2015-04-07T18:22:43.167897Z", 
            "content": 1, 
            "accounts": [
                1
            ], 
            "community": []
        }
    ]
}
```
---
#####Request: GET @auth-required
```http
/api/v1/account/<pk>/communities/
```
Returns a paginated list of communities the authenticated user has interacted with, sorted by most recent
```json
{
    "count": 1, 
    "next": null, 
    "previous": null, 
    "results": [
        {
            "id": 1, 
            "community": "Yoloswag", 
            "community_description": "Where big pimps chill", 
            "lead_image_url": "", 
            "participation_rate": null, 
            "created_at": "2015-04-04T04:30:55.535874Z", 
            "updated_at": "2015-04-07T18:23:47.544967Z", 
            "accounts": [
                1
            ], 
            "topics": [
                1
            ]
        }
    ]
}
```
---
#####Request: GET @auth-required
```http
/api/v1/me/
```
Returns the currently authenticated user account's object

```json
{
    "id": 1, 
    "last_login": "2015-04-04T04:04:02.226792Z", 
    "username": "avatchinsky", 
    "email": "adrian@adrian.com", 
    "first_name": "Adrian", 
    "last_name": "Vatchinsky", 
    "profile_picture_url": "http://placehold.it/150x150", 
    "is_admin": true, 
    "is_manager": false, 
    "created_at": "2015-04-04T04:03:50.932471Z", 
    "updated_at": "2015-04-07T18:20:20.098732Z"
}
```
---
#### Topics
#####Request: GET @auth-required
```http
/api/v1/topics/
```
#####Response
Paginated result of all topics
```json
{
    "count": 2, 
    "next": null, 
    "previous": null, 
    "results": [
        {
            "id": 1, 
            "topic": "News", 
            "lead_image_url": "", 
            "created_at": "2015-04-04T04:04:37.638011Z", 
            "updated_at": "2015-04-04T04:04:37.638047Z", 
            "accounts": []
        }, 
    ]
}
```
---
#####Request: GET PUT DELETE @auth-required
```http
/api/v1/topic/<pk>/
```
#####Response
Get topic based off of its ```pk```
```json
{
    "id": 1, 
    "topic": "News", 
    "lead_image_url": "", 
    "created_at": "2015-04-04T04:04:37.638011Z", 
    "updated_at": "2015-04-04T04:04:37.638047Z", 
    "accounts": []
}
```
---
#####Request: GET @auth-required
```http
/api/v1/topic/<pk>/communities/
```
#####Response
Paginated result of all topic communities
```json
{
    "count": 2, 
    "next": null, 
    "previous": null, 
    "results": [
        {
            "id": 1, 
            "community": "Yoloswag", 
            "community_description": "Where big pimps chill", 
            "lead_image_url": "", 
            "participation_rate": null, 
            "created_at": "2015-04-04T04:30:55.535874Z", 
            "updated_at": "2015-04-07T18:23:47.544967Z", 
            "accounts": [
                1
            ], 
            "topics": [
                1
            ]
        }, 
    ]
}
```
---

#### Content
#####Request: GET @auth-required
```http
/api/v1/accounts/
```
#####Response
Paginated result of all content. ```next``` and ```previous``` contain ```urls``` to the 
following pages.
```json
{
    "count": 5, 
    "next": null, 
    "previous": null, 
    "results": [
        {
            "id": 5, 
            "url": "http://www.engadget.com/2015/04/03/dyre-wolf-attack-swipes-1-million-in-wire-transfers/", 
            "domain": "www.engadget.com", 
            "title": "Dyre Wolf attack swipes $1 million in wire transfers", 
            "excerpt": "Hackers continue their brazen attacks on organizations and are even having their victims call them on the phone to hustle them out of their company's money. That's what IBM's Security Intelligence&hellip;", 
            "content": "<div id=\"body\">\r\n\t\t \r\n\t\t \r\n\t\t \r\n\t\t<div class=\"copy post-body \">\r\n    <div class=\"article-content\"> \r\n\t\t        \r\n\r\n<center><img src=\"http://o.aolcdn.com/dims-shared/dims3/GLOB/crop/938x535+0+0/resize/630x359!/format/jpg/quality/85/http://o.aolcdn.com/hss/storage/midas/190dc9f2ef83ea946cb2bbc5922d34e7/201785065/0403_dyrewolf.jpg\" alt=\"\"></center>\r\n\r\n\r\n\r\n<p class=\"p1\">Hackers continue their brazen attacks on organizations and are even having their victims call them on the phone to hustle them out of their company's money. That's what <a href=\"http://securityintelligence.com/dyre-wolf/#.VR8RFZTF_Aq\">IBM's Security Intelligence</a> division has discovered while researching a malware-based attack they have dubbed The Dyre Wolf that's responsible for stealing more than $1 million. The coordinated campaign uses targeted spear phishing emails, malware and good ol' chatting-on-the-phone social engineering to go after organizations that use wire transfers.</p>\r\n\r\n \r\n\t\r\n\t<p class=\"p1\">According to IBM threat researchers, the attack starts with a single user opening an infected email attachment. Once opened, that malware contacts the attacker's server then downloads and installs the Dyre malware which hijacks the user's address book and mails itself throughout the organization.</p>\r\n\r\n\r\n\r\n<p class=\"p1\">Then things get real fun. When a victim with an infected computer attempts to log in to a banking site monitored by the malware, it throws up a new screen that says that the site is experiencing issues and presents a phone number for that person to call to make their transaction. Once the attackers have all the information, a wire transfer is made that runs through a series of international banks to thwart authorities.</p>\r\n\r\n\r\n\r\n<p class=\"p1\">The entire attack relies on social engineering. The victims have to open the initial attachment and make the phone call that could cost their company a lot of money. This circumvents passwords and two-factor authentication because it goes around the digital entrance and gets critical information directly from the victim. IBM recommends companies train their employees to never open or click suspicious attachments or links and to remind employees that banks will never ask them for their banking credentials.</p>\r\n\r\n<p class=\"p1\"><img src=\"http://o.aolcdn.com/dims-shared/dims3/GLOB/crop/1442x1110+0+0/resize/630x485!/format/jpg/quality/85/http://o.aolcdn.com/hss/storage/midas/2bb87742c761e76093e523be4a912305/201785067/0403_DyerWolfAttackSteps.jpg\" alt=\"\"></p>\r\n\r\n<p class=\"p1\">[Image Credit: IBM]</p>   \r\n\r\n  <div id=\"instream-container\" class=\"advis-ad\">\r\n    <div id=\"instream\" class=\"advis\">\r\n    \r\n    </div>\r\n  </div>\r\n        \r\n        \r\n        <p class=\"read-more\">\r\n            \r\n            <a class=\"show-comments hidden enable clink_21161244\">\r\n                <span class=\"text\"> Hide Comments</span>\r\n                <span class=\"livefyre-commentcount\">0</span>Comments</a>\r\n            \r\n            <span class=\"social-tools\">\r\n                <a class=\"aol-share-placeholder-all\" href=\"mailto:yourfriend@email.com?subject=Dyre+Wolf+attack+swipes+%241+million+in+wire+transfers&amp;body=http://www.engadget.com/2015/04/03/dyre-wolf-attack-swipes-1-million-in-wire-transfers/\" title=\"Dyre Wolf attack swipes $1 million in wire transfers\"></a>\r\n\r\n            </span>\r\n            <span class=\"share-more\">\r\n                <a class=\"aol-share-placeholder-all\" href=\"mailto:yourfriend@email.com?subject=Dyre+Wolf+attack+swipes+%241+million+in+wire+transfers&amp;body=http://www.engadget.com/2015/04/03/dyre-wolf-attack-swipes-1-million-in-wire-transfers/\" title=\"Dyre Wolf attack swipes $1 million in wire transfers\"></a>\r\n            </span>\r\n        </p>\r\n        \r\n\r\n        <div id=\"comments\" class=\"comments_21161244\">\r\n            <div id=\"livefyre_21161244\"></div>\r\n            \r\n        </div>\r\n        \r\n\r\n \r\n\t\t \r\n\t\t<div id=\"grv-personalization-14\"></div>\r\n\r\n\r\n<div id=\"articlebottom\"></div>\r\n\r\n\r\n<div id=\"mobile-on-vis\">\r\n\r\n</div> \r\n\t\t    </div>\r\n    \r\n<div class=\"rail-ad rail-ad-topper \">\r\n    <div class=\"rail-infinite\">\r\n        <div id=\"ad_21161244\"></div>\r\n        \r\n        \r\n        <div class=\"rail-collection-main\">\r\n\r\n\r\n             \r\n<aside class=\"module rail-latest beacon-ping-cids\">\r\n<h3 class=\"hed green\">Featured Stories</h3><div id=\"p21159397\"><article class=\"feature beacon-ping-plids\">\r\n\r\n<a href=\"http://www.engadget.com/2015/04/03/hp-spectre-x360-review/\"><img src=\"http://o.aolcdn.com/dims-global/dims/GLOB/5/300/160/90/http://o.aolcdn.com/hss/storage/midas/21a5f3f136fe6c31e93ef8ce2715e921/201762599/P1010103_thumbnail.jpg\" class=\"feature-image\" alt=\"Post Image\"></a>\r\n\r\n<header class=\"feature-overlay\">\r\n<h3 class=\"feature-title\"><a href=\"http://www.engadget.com/2015/04/03/hp-spectre-x360-review/\"><span id=\"pt21159397\">HP Spectre x360 review: What happens when Microsoft helps build a laptop?</span></a></h3>\r\n<div class=\"meta\"><time datetime=\"Fri, 03 Apr 2015 00:00:00 -0400\" class=\"time-stamp\">8 hours ago</time> <span class=\"comment-count\"><a href=\"http://www.engadget.com/2015/04/03/hp-spectre-x360-review/#comments\"><i class=\"s-comment-bubble-black-12\"></i> <span class=\"livefyre-commentcount\">0</span></a></span></div>\r\n</header>\r\n</article></div><div id=\"p21160005\"><article class=\"feature beacon-ping-plids\">\r\n\r\n<header class=\"feature-overlay\">\r\n<h3 class=\"feature-title\"><a href=\"http://www.engadget.com/2015/04/02/heres-what-our-readers-think-of-the-amazon-echo/\"><span id=\"pt21160005\">Here's what our readers think of the Amazon Echo</span></a></h3>\r\n<div class=\"meta\"><time datetime=\"Thu, 02 Apr 2015 00:00:00 -0400\" class=\"time-stamp\">1 day ago</time> <span class=\"comment-count\"><a href=\"http://www.engadget.com/2015/04/02/heres-what-our-readers-think-of-the-amazon-echo/#comments\"><i class=\"s-comment-bubble-black-12\"></i> <span class=\"livefyre-commentcount\">0</span></a></span></div>\r\n</header>\r\n</article></div><div id=\"p21157197\"><article class=\"feature beacon-ping-plids\">\r\n\r\n<header class=\"feature-overlay\">\r\n<h3 class=\"feature-title\"><a href=\"http://www.engadget.com/2015/04/02/samsung-galaxy-s6-and-s6-edge-review/\"><span id=\"pt21157197\">Galaxy S6 and S6 Edge review: Samsung's best phones in years</span></a></h3>\r\n<div class=\"meta\"><time datetime=\"Thu, 02 Apr 2015 00:00:00 -0400\" class=\"time-stamp\">1 day ago</time> <span class=\"comment-count\"><a href=\"http://www.engadget.com/2015/04/02/samsung-galaxy-s6-and-s6-edge-review/#comments\"><i class=\"s-comment-bubble-black-12\"></i> <span class=\"livefyre-commentcount\">0</span></a></span></div>\r\n</header>\r\n</article></div><div id=\"p21157957\"><article class=\"feature beacon-ping-plids\">\r\n\r\n<header class=\"feature-overlay\">\r\n<h3 class=\"feature-title\"><a href=\"http://www.engadget.com/2015/03/31/macbook-pro-with-retina-display-review-13-inch-2015/\"><span id=\"pt21157957\">MacBook Pro with Retina display review (13-inch, 2015)</span></a></h3>\r\n<div class=\"meta\"><time datetime=\"Tue, 31 Mar 2015 00:00:00 -0400\" class=\"time-stamp\">3 days ago</time> <span class=\"comment-count\"><a href=\"http://www.engadget.com/2015/03/31/macbook-pro-with-retina-display-review-13-inch-2015/#comments\"><i class=\"s-comment-bubble-black-12\"></i> <span class=\"livefyre-commentcount\">0</span></a></span></div>\r\n</header>\r\n</article></div><div id=\"p21159619\"><article class=\"feature beacon-ping-plids\">\r\n\r\n<header class=\"feature-overlay\">\r\n<h3 class=\"feature-title\"><a href=\"http://www.engadget.com/2015/03/31/google-budget-chromebooks-asus-flip/\"><span id=\"pt21159619\">Google reveals budget Chromebooks including a $249 ASUS convertible</span></a></h3>\r\n<div class=\"meta\"><time datetime=\"Tue, 31 Mar 2015 00:00:00 -0400\" class=\"time-stamp\">3 days ago</time> <span class=\"comment-count\"><a href=\"http://www.engadget.com/2015/03/31/google-budget-chromebooks-asus-flip/#comments\"><i class=\"s-comment-bubble-black-12\"></i> <span class=\"livefyre-commentcount\">0</span></a></span></div>\r\n</header>\r\n</article></div><div id=\"p21159630\"><article class=\"feature beacon-ping-plids\">\r\n\r\n<header class=\"feature-overlay\">\r\n<h3 class=\"feature-title\"><a href=\"http://www.engadget.com/2015/03/31/google-chromebit/\"><span id=\"pt21159630\">Google puts Chrome OS on your TV with its own HDMI stick</span></a></h3>\r\n<div class=\"meta\"><time datetime=\"Tue, 31 Mar 2015 00:00:00 -0400\" class=\"time-stamp\">3 days ago</time> <span class=\"comment-count\"><a href=\"http://www.engadget.com/2015/03/31/google-chromebit/#comments\"><i class=\"s-comment-bubble-black-12\"></i> <span class=\"livefyre-commentcount\">0</span></a></span></div>\r\n</header>\r\n</article></div><div id=\"p21156583\"><article class=\"feature beacon-ping-plids\">\r\n\r\n<header class=\"feature-overlay\">\r\n<h3 class=\"feature-title\"><a href=\"http://www.engadget.com/2015/03/31/microsoft-surface-3/\"><span id=\"pt21156583\">Microsoft's new Surface 3 tablet runs full Windows, not RT</span></a></h3>\r\n<div class=\"meta\"><time datetime=\"Tue, 31 Mar 2015 00:00:00 -0400\" class=\"time-stamp\">3 days ago</time> <span class=\"comment-count\"><a href=\"http://www.engadget.com/2015/03/31/microsoft-surface-3/#comments\"><i class=\"s-comment-bubble-black-12\"></i> <span class=\"livefyre-commentcount\">0</span></a></span></div>\r\n</header>\r\n</article></div></aside>\r\n\r\n\r\n\r\n\r\n<aside class=\"module rail-latest\">\r\n\t<h3 class=\"hed green\">Sponsored Content</h3>\r\n\t<div id=\"railSetInView\" class=\"rail-set-in-view-ad\"></div>\r\n\t\r\n</aside>\r\n\r\n  \r\n            <aside class=\"module\" id=\"rail-asl\"></aside> \r\n\t   \r\n\r\n\t\t\t<div class=\"promoted module\">\r\n\t\t\t\t<div class=\"compare-gadgets-feature\">\r\n\t\t\t\t\t<h3>Compare Your Gadgets</h3>\r\n\t\t\t\t\t<a href=\"http://www.engadget.com/compare\"><img src=\"http://www.blogsmithmedia.com/www.engadget.com/media/compare-module.jpg\" alt=\"Compare Your Gadgets\"></a>\r\n\t\t\t\t\t<p>Instantly <strong>compare products</strong> side by side and see which one is best for you!</p>\r\n\t\t\t\t\t<p><a href=\"http://www.engadget.com/compare\" class=\"try-it\">Try it now →</a></p>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t\r\n\r\n        </div>\r\n\r\n        <div class=\"onvis\" id=\"adSkyScraper\"></div>\r\n\r\n    </div>\r\n    \r\n    \r\n</div>\r\n\r\n</div>\r\n \r\n\t\t \r\n\t\t<div id=\"p21161244\"><a href=\"http://www.engadget.com/2015/04/03/daily-roundup-hp-spectre-x360-review-spying-games-and-more/\" class=\"amp-eternal-article loading\">Daily Roundup: HP Spectre x360 review, spying games and more!</a>\r\n</div> \r\n\t</div>\r\n\r\n\t\r\n\t", 
            "lead_image_url": "http://o.aolcdn.com/dims-global/dims/GLOB/5/300/160/90/http://o.aolcdn.com/hss/storage/midas/21a5f3f136fe6c31e93ef8ce2715e921/201762599/P1010103_thumbnail.jpg", 
            "date_published": null, 
            "word_count": 413, 
            "view_count": 1, 
            "share_count": null, 
            "created_at": "2015-04-04T05:17:55.805749Z", 
            "community": [
                2
            ]
        }, 
    ]
}
```
---
#### Bits
