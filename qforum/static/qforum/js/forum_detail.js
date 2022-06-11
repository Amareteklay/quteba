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
                 console.log('success', response)
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
                 console.log('success', response)
                 document.getElementById('num-down-votes').innerHTML = response['downvotes']
                 document.getElementById('num-up-votes').innerHTML = response['upvotes']
             },
             error: function(error) {
                 console.log('error', error)
             }
         });
     });
 });