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
     $('.liking').click(function(e) {
         e.preventDefault();
         var pk = document.getElementById('likes').getAttribute('data-value');
         var button = $(this).find("span");
         $.ajax({
             type: 'POST',
             url: '/forum/like/',
             data: {
                 pk: pk,
                 csrfmiddlewaretoken: csrftoken,
                 action: 'liking',
             },
             success: function(response) {
                 button.html(response['likes'])
                 document.getElementById('num-dislikes').innerHTML = response['dislikes']
             },
             error: function(error) {
                 console.log('error', error)
             }
         });
     });
 });

 // Dislike functionality

 $(document).ready(function() {
     $('.disliking').click(function(e) {
         e.preventDefault();
         var pk = document.getElementById('dislikes').getAttribute('data-value');
         var button = $(this).find("span");
         $.ajax({
             type: 'POST',
             url: '/forum/dislike/',
             data: {
                 pk: pk,
                 csrfmiddlewaretoken: csrftoken,
                 action: 'disliking',
             },
             success: function(response) {
                 button.html(response['dislikes'])
                 document.getElementById('num-likes').innerHTML = response['likes']
             },
             error: function(error) {
                 console.log('error', error)
             }
         });
     });
 });


 // Add comment with ajax
 /* const commentForm = document.getElementsByClassName('comment-form')
 $(document).ready(function() {
     for (let form of commentForm) {
         form.addEventListener('submit', e => {
             e.preventDefault();
             var commentBox = document.getElementById('comment-box');
             var replyBox = document.getElementById('reply-box');
             var content = form.getElementsByTagName('textarea')[0];
             console.log(content.value)
             var pk = form.getAttribute('data-thread');
             var parent = form.getAttribute('data-parent');
             console.log(parent)
             console.log(pk)
             console.log('So far so good')
             $.ajax({
                 type: 'POST',
                 url: url,
                 data: {
                     'csrfmiddlewaretoken': csrftoken,
                     content: content.value,
                     parent: parent,
                     pk: pk,
                 },
                 success: function(response) {
                     if (parent == 0) {
                         commentBox.insertAdjacentHTML('afterbegin', `
                <a class="text-black" href="#">
                <img class="rounded-circle article-img profile-img" src="${response.profile}">
                ${response.name}</a>
              <span class="op-6 text-muted">${response.created}</span>
              {% if request.user == comment.name %}
              <span class="op-6 px-3 text-muted"><i class="fa-solid fa-pen-to-square"></i></span>
              <span class="op-6 text-muted"><i class="fa-solid fa-trash small"></i></span>
              {% endif %}
              <p class="px-3 mt-2"> ${response.content}</p>
              <div class="col-1 d-inline-block" id="likes" data-value="${response.pk}">
                <a class="btn liking" value="like" role="button">
                    <i class="fa-solid fa-thumbs-up"></i>
                    <span id="num-likes">${response.likes}</span>
                </a>
              </div>
              <div class="col-1 d-inline-block" id="dislikes" data-value="${response.pk}">
                <a class="btn disliking" value="dislike" role="button">
                    <i class="fa-solid fa-thumbs-down"></i>
                    <span id="num-dislikes">${response.dislikes}</span>
                </a>
              </div>
              {% if user != comment.name %}
              <button class="btn btn-sm d-inline-block" data-bs-toggle="collapse" data-bs-target="#reply-form-${response.pk}" aria-controls="reply-form-${response.pk}">
                <i class="fa-solid fa-comment text-muted"></i> <span>Reply</span></button>
              {% endif %}
               `);
                         $('.add-comment-modal').modal('hide');
                     } else {
                         replyBox.insertAdjacentHTML('afterbegin', `
                <div>
            <a class="text-black" href="#">
            <span class="op-6 text-muted">{{ comment.created|timesince }} ago</span>
            
            <span class="op-6 px-3 text-muted"><i class="fa-solid fa-pen-to-square"></i></span>
            <span class="op-6 text-muted"><i class="fa-solid fa-trash small"></i></span>
          
            <p>Parent: {{comment.parent.id}}</p>
            <p class="px-3 mt-2">${response.content}</p>
                        <h1>This is from new reply </h1>
            <!-- Like unlike ajax -->
            <div class="col-1 d-inline-block" id="likes" data-value="{{comment.id}}">
                <a class="btn liking" value="like" role="button">
                    <i class="fa-solid fa-thumbs-up"></i>
                    <span id="num-likes">{{ comment.no_of_likes }}</span>
                </a>
            </div>
            <div class="col-1 d-inline-block" id="dislikes" data-value="{{comment.id}}">
                <a class="btn disliking" value="dislike" role="button">
                    <i class="fa-solid fa-thumbs-down"></i>
                    <span id="num-dislikes">{{ comment.no_of_dislikes }}</span>
                </a>
            </div>
        </div>
        `);
                     }
                     form.hideForm;
                     form.reset();
                     alert('Working!')
                 },
                 error: function(error) {
                     console.log('Error: ', error);
                 },
             });
         });
     }
 }); */