 const getCookie = (name) => {
     let cookieValue = null;
     if (document.cookie && document.cookie !== '') {
         const cookies = document.cookie.split(';');
         for (let i = 0; i < cookies.length; i++) {
             const cookie = cookies[i].trim();
             if (cookie.substring(0, name.length + 1) === (name + '=')) {
                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                 break;
             }
         }
     }
     return cookieValue;
 };
 const csrftoken = getCookie('csrftoken');

 document.addEventListener('DOMContentLoaded', function() {
     const navbarItems = document.getElementsByClassName('nav-link');
     for (let i = 0; i < navbarItems.length; i++) {
         if (navbarItems[i].href === window.location.href) {
             navbarItems[i].classList.add('active-menu');
         }
     }
 });

 function handleReply(response_id) {
     const reply_form_container = document.querySelector(`#reply-form-container-${response_id}`);
     if (reply_form_container) {
         reply_form_container.style.display = 'block';
     }
 }

 function handleCancel(response_id) {
     const reply_form_container = document.querySelector(`#reply-form-container-${response_id}`);
     if (reply_form_container) {
         reply_form_container.style.display = 'none';
     }
 }

 function displayForm() {
     document.querySelector('#comment-form').classList.add('text-muted');
     document.querySelector('.comment-form').style.display = 'block';
 }

 function displayCommentReplyForm() {
     document.querySelector('.comment-form').style.display = 'block';
 }

 function hideForm() {
     let form_btn = document.querySelector('#comment-form');
     form_btn.classList.remove('text-muted');
     form_btn.classList.add('d-inline-block');
     document.querySelector('.comment-form').style.display = 'none';
 }

 function displayThreadForm() {
     let thread_form = document.querySelector('#question-form');
     thread_form.style.display = 'block';
     thread_form.classList.add('text-center');
 }

 function hideForumButton() {
     let btn_forum = document.querySelector('#btn-create-forum');
     btn_forum.style.display = 'none';
 }


 const url = window.location.href;

 $(document).ready(function() {
     $('.voting-up').click(function(e) {
         e.preventDefault();
         var slug = document.getElementById('up-votes').getAttribute('data-value');
         $.ajax({
             type: 'POST',
             url: '/forum/upvote/',
             data: {
                 slug: slug,
                 csrfmiddlewaretoken: csrftoken,
                 action: 'votingup',
             },
             success: function(response) {
                 document.getElementById('num-up-votes').innerHTML = response.upvotes;
                 document.getElementById('num-down-votes').innerHTML = response.downvotes;
             },
             error: function(error) {
                 console.log('error', error);
             }
         });
     });
 });

 $(document).ready(function() {
     $('.voting-down').click(function(e) {
         e.preventDefault();
         var slug = document.getElementById('down-votes').getAttribute('data-value');
         $.ajax({
             type: 'POST',
             url: '/forum/downvote/',
             data: {
                 slug: slug,
                 csrfmiddlewaretoken: csrftoken,
                 action: 'votingdown',
             },
             success: function(response) {
                 document.getElementById('num-down-votes').innerHTML = response.downvotes;
                 document.getElementById('num-up-votes').innerHTML = response.upvotes;
             },
             error: function(error) {
                 console.log('error', error);
             }
         });
     });
 });

 // Like functionality

 $(document).ready(function() {
     $('.like-dislike').each(function() {
         var likeDislike = $(this);
         likeDislike.find('.likes').on('click', function(e) {
             e.preventDefault();
             var pk = likeDislike.attr('data-value');
             console.log(pk);
             console.log('Liked');
             var likeBtn = likeDislike.find("span")[0];
             var dislikeBtn = likeDislike.find("span")[1];
             console.log(likeBtn);
             $.ajax({
                 type: 'POST',
                 url: '/forum/like/',
                 data: {
                     pk: pk,
                     csrfmiddlewaretoken: csrftoken,
                     action: 'liking',
                 },
                 success: function(response) {
                     likeBtn.innerHTML = response.likes;
                     dislikeBtn.innerHTML = response.dislikes;
                 },
                 error: function(error) {
                     console.log('error', error);
                 }
             });
         });
     });
 });

 // Dislike functionality

 $(document).ready(function() {
     $('.like-dislike').each(function() {
         var likeDislike = $(this);
         likeDislike.find('.dislikes').on('click', function(e) {
             e.preventDefault();
             var pk = likeDislike.attr('data-value');
             console.log(pk);
             console.log('Disliked');
             var likeBtn = likeDislike.find("span")[0];
             var dislikeBtn = likeDislike.find("span")[1];
             $.ajax({
                 type: 'POST',
                 url: '/forum/like/',
                 data: {
                     pk: pk,
                     csrfmiddlewaretoken: csrftoken,
                     action: 'disliking',
                 },
                 success: function(response) {
                     dislikeBtn.innerHTML = response.dislikes;
                     likeBtn.innerHTML = response.likes;
                 },
                 error: function(error) {
                     console.log('error', error);
                 }
             });
         });
     });
 });

 //Create forum
 $(document).ready(function() {
     const threadBox = document.getElementById('thread-box');
     const url = window.location.href;
     console.log('sfsg');

     $('#create-forum-form').submit(function(e) {
         e.preventDefault();
         var topic = document.getElementById('id_topic');
         var description = document.getElementById('id_description');
         var category = document.getElementById('id_category');
         console.log('sfsg');
         $.ajax({
             type: 'POST',
             dataType: 'json',
             url: '',
             data: {
                 'csrfmiddlewaretoken': csrftoken,
                 'topic': topic.value,
                 'description': description.value,
                 'category': category.value,
             },
             cache: false,
         }).done(function(response) {
             threadBox.insertAdjacentHTML('afterbegin', `
        <div class="card shadow-lg row-hover pos-relative px-3 mb-3 rounded-2 left-border">
        <div class="row pb-3 align-items-center">
        <div class="col-md-8 mb-3 mb-sm-0">
            <img class="rounded-circle article-img profile-img" src="${response.profile}">
            <a class="text-black" href="#"> ${response.name}</a> <span class="op-6 text-muted">
            | ${response.created}</span>
            <h5 class="pt-3 px-3">
                <a href="${url}${response.slug}" class="text-primary">${response.topic}</a>
            </h5>
            <div class="px-3">
                ${response.description}
            </div>
        </div>
        <div class="px-4">
            <span class="d-inline-block text-sm text-success"> <i class="fa-solid fa-caret-up"></i>
                 </span>
            <span class="d-inline-block text-sm text-danger mx-3"> <i class="fa-solid fa-caret-down"></i>
                 </span>
            <span class="d-inline-block text-sm mx-3"><i class="fa-solid fa-comments"></i>
                </span>
        </div>
    </div>
</div> `);
             $('#addForumModal').modal('hide');
             $(this).trigger('reset');
         });
     });
 });

 // Comment and reply
 $(document).ready(function() {
     const commentForm = document.getElementsByClassName('comment-form');
     for (let form of commentForm) {
         form.addEventListener('submit', e => {
             e.preventDefault();
             var content = form.getElementsByTagName('textarea')[0];
             var pk = form.getAttribute('data-thread');
             console.log(pk);
             var commentBox = document.querySelector('.comment-box');
             console.log(commentBox);
             var parent = form.getAttribute('data-parent');

             $.ajax({
                 type: 'POST',
                 url: '',
                 data: {
                     'csrfmiddlewaretoken': csrftoken,
                     content: content.value,
                     parent: parent,
                     pk: pk,
                 },
                 success: function(response) {
                     if (parent == 0) {
                         commentBox.insertAdjacentHTML('afterbegin', `
                <div class="pt-2 shadow border-bottom">
    <a class="text-black" href="{% url 'profile' %}">
        <img class="rounded-circle article-img profile-img" src="${response.profile}">
        ${response.name}</a>
    <span class="op-6 text-muted">${response.created}</span>
    <p class="px-3 mt-2"> ${response.content}</p>
    </div>
    `);
                         $('.add-comment-modal').modal('hide');
                     } else {
                         form.closest('.form-box').insertAdjacentHTML('afterend', `
                         <div class="left-indent mt-4 shadow">
                         <div class="mb-2">                     
        <a class="text-black" href="#">
            <img class="rounded-circle article-img profile-img" src="${response.profile}">
            ${response.name}</a>
        <span class="op-6 text-muted">${response.created}</span>
        <p class="px-3 mt-2">${response.content}</p>
        </div>
    </div>
    `);
                     }
                     $('.form-box').modal('hide');
                     form.reset();
                 },
                 error: function(error) {
                     console.log('Error: ', error);
                 },
             });
         });
     }
 });