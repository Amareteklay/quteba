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

const newBox = document.getElementById("new-box")
const btnForum = document.getElementById("btn-forum")
btnForum.addEventListener('click', function() {
    newBox.style.backgroundColor = 'red';
});

newTForm = document.getElementById('create-forum-form')
topic = document.getElementById('id_topic')
description = document.getElementById('id_description')
category = document.getElementById('id_category')

const csrf = document.getElementsByName('csrfmiddlewaretoken')
console.log(csrf[0].value)

newTForm.addEventListener('submit', e => {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '/forum/',
        data: {
            'csrfmiddlewaretoken': csrf[0].value,
            'topic': topic.value,
            'description': description.value,
            'category': category.value,
        },
        success: function(response) {
            console.log('Success: ', response);
            newBox.insertAdjacentHTML('afterbegin',
                `<h1 class = "text-success text-center" > 
                ${response.topic} </h1>`
            )
        },
        error: function(error) {
            console.log('Error: ', error);
        }
    });
});