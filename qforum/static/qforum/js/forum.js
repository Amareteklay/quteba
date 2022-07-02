 const getCookie = (name) => {
     let cookieValue = null;
     if (document.cookie && document.cookie !== '') {
         const cookies = document.cookie.split(';');
         for (let i = 0; i < cookies.length; i++) {
             const cookie = cookies[i].trim();
             // Does this cookie string begin with the name we want?
             if (cookie.substring(0, name.length + 1) === (name + '=')) {
                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                 break;
             }
         }
     }
     return cookieValue;
 }
 const csrftoken = getCookie('csrftoken');


 function handleReply(response_id) {
     const reply_form_container = document.querySelector(`#reply-form-container-${response_id}`)
     if (reply_form_container) {
         reply_form_container.style.display = 'block';
     }
 }

 function handleCancel(response_id) {
     const reply_form_container = document.querySelector(`#reply-form-container-${response_id}`)
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
     thread_form.style.display = 'block'
     thread_form.classList.add('text-center');
 }

 function hideForumButton() {
     let btn_forum = document.querySelector('#btn-create-forum');
     btn_forum.style.display = 'none';
 }


 const url = window.location.href

 $(document).ready(function() {
     $('.voting-up').click(function(e) {
         e.preventDefault();
         var slug = document.getElementById('up-votes').getAttribute('data-value');
         var button = $(this).attr("value");
         $.ajax({
             type: 'POST',
             url: '/forum/upvote/',
             data: {
                 slug: slug,
                 csrfmiddlewaretoken: csrftoken,
                 action: 'votingup',
             },
             success: function(response) {
                 document.getElementById('num-up-votes').innerHTML = response['upvotes']
                 document.getElementById('num-down-votes').innerHTML = response['downvotes']
             },
             error: function(error) {
                 console.log('error', error)
             }
         });
     });
 });

 $(document).ready(function() {
     $('.voting-down').click(function(e) {
         e.preventDefault();
         var slug = document.getElementById('down-votes').getAttribute('data-value');
         var button = $(this).attr("value");
         $.ajax({
             type: 'POST',
             url: '/forum/downvote/',
             data: {
                 slug: slug,
                 csrfmiddlewaretoken: csrftoken,
                 action: 'votingdown',
             },
             success: function(response) {
                 document.getElementById('num-down-votes').innerHTML = response['downvotes']
                 document.getElementById('num-up-votes').innerHTML = response['upvotes']
             },
             error: function(error) {
                 console.log('error', error)
             }
         });
     });
 });

 // Like functionality

 $(document).ready(function() {
     $('.likes').each(function() {
         $(this).on('click', function(e) {
             e.preventDefault();
             var pk = $(this).attr('data-value')
             console.log(pk)
             var likeBtn = $(this).find("span");
             $.ajax({
                 type: 'POST',
                 url: '/forum/like/',
                 data: {
                     pk: pk,
                     csrfmiddlewaretoken: csrftoken,
                     action: 'liking',
                 },
                 success: function(response) {
                     likeBtn.html(response['likes'])
                     document.getElementsByClassName('num-dislikes').innerHTML = response['dislikes']
                 },
                 error: function(error) {
                     console.log('error', error)
                 }
             });
         });
     });
 });

 // Dislike functionality

 $(document).ready(function() {
     $('.dislikes').each(function() {
         $(this).on('click', function(e) {
             e.preventDefault();
             var pk = $(this).attr('data-value')
             console.log(pk)
             var dislikeBtn = $(this).find("span");
             $.ajax({
                 type: 'POST',
                 url: '/forum/dislike/',
                 data: {
                     pk: pk,
                     csrfmiddlewaretoken: csrftoken,
                     action: 'disliking',
                 },
                 success: function(response) {
                     dislikeBtn.html(response['dislikes'])
                     document.getElementsByClassName('num-likes').innerHTML = response['likes']
                 },
                 error: function(error) {
                     console.log('error', error)
                 }
             });
         });
     });
 });

 //Create forum
 $(document).ready(function() {
     const threadBox = document.getElementById('thread-box')
     const url = window.location.href
     console.log('sfsg')
     /* const getCookie = (name) => {
         let cookieValue = null;
         if (document.cookie && document.cookie !== '') {
             const cookies = document.cookie.split(';');
             for (let i = 0; i < cookies.length; i++) {
                 const cookie = cookies[i].trim();
                 // Does this cookie string begin with the name we want?
                 if (cookie.substring(0, name.length + 1) === (name + '=')) {
                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                     break;
                 }
             }
         }
         return cookieValue;
     }
     const csrftoken = getCookie('csrftoken'); */

     $('#create-forum-form').submit(function(e) {
         e.preventDefault();
         var topic = document.getElementById('id_topic')
         var description = document.getElementById('id_description')
         var category = document.getElementById('id_category')
         console.log('sfsg')
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
            <span class="d-inline-block text-sm text-muted"> <i class="fa-solid fa-caret-up"></i>
                 </span>
            <span class="d-inline-block text-sm text-muted mx-3"> <i class="fa-solid fa-caret-down"></i>
                 </span>
            <span class="d-inline-block text-sm text-muted mx-3"><i class="fa-solid fa-comments"></i>
                </span>
        </div>
    </div>
</div> `)
             $('#addForumModal').modal('hide');
             $(this).trigger('reset');
         });
     });
 })
 // Comment and reply

 $(document).ready(function() {
     console.log('sfsg')
     const commentForm = document.getElementsByClassName('comment-form')
     console.log('sfsg')
     for (let form of commentForm) {
         const url = window.location.href
         form.addEventListener('submit', e => {
             e.preventDefault();
             const commentBox = document.getElementById('comment-box');
             var replyBox = document.getElementById('reply-box');
             var content = form.getElementsByTagName('textarea')[0];
             var pk = form.getAttribute('data-thread');
             console.log(pk);
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
    <div>
        <a class="text-black" href="#">
            <img class="rounded-circle article-img profile-img" src="${response.profile}">
            ${response.name}</a>
        <span class="op-6 text-muted">${response.created}</span>
        <p class="px-3 mt-2">${response.content}</p>
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