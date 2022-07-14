 // Get cookies and fetch csrf token
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

 // Voting up forums
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

 // Voting down forums
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
             var likeBtn = likeDislike.find("span")[0];
             var dislikeBtn = likeDislike.find("span")[1];
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

 //Create forum entry
 $(document).ready(function() {
     const threadBox = document.getElementById('thread-box');
     const url = window.location.href;

     $('#create-forum-form').submit(function(e) {
         e.preventDefault();
         var topic = document.getElementById('id_topic');
         var description = document.getElementById('id_description');
         var category = document.getElementById('id_category');

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
         const cform = form;
         cform.addEventListener('submit', e => {
             e.preventDefault();
             var content = cform.getElementsByTagName('textarea')[0];
             var pk = cform.getAttribute('data-thread');
             var commentBox = document.querySelector('.comment-box');
             var parent = cform.getAttribute('data-parent');

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
                         $('.comment-prompt').hide();
                         commentBox.insertAdjacentHTML('afterbegin', `
                <div class="pt-2 shadow border-bottom">
    <a class="text-black" href="{% url 'profile' %}">
        <img class="rounded-circle article-img profile-img" src="${response.profile}">
        ${response.name}</a>
    <span class="op-6">${response.created}</span>
    <p class="px-3 mt-2"> ${response.content}</p>
    </div>
    `);
                         $('.add-comment-modal').modal('hide');
                     } else {
                         cform.closest('.form-box').insertAdjacentHTML('afterend', `
                         <div class="left-indent mt-4 shadow">
                         <div class="mb-2">                     
        <a class="text-black" href="#">
            <img class="rounded-circle article-img profile-img" src="${response.profile}">
            ${response.name}</a>
        <span class="op-6">${response.created}</span>
        <p class="px-3 mt-2">${response.content}</p>
        </div>
    </div>
    `);
                     }
                     $('.form-box').modal('hide');
                     cform.reset();
                 },
                 error: function(error) {
                     console.log('Error: ', error);
                 },
             });
         });
     }
 });