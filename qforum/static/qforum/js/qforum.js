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


newTForm = document.getElementById('create-forum-form')
topic = document.getElementById('id_topic')
description = document.getElementById('id_description')
category = document.getElementById('id_category')

const csrf = document.getElementsByName('csrfmiddlewaretoken')
const threadBox = document.getElementById('thread-box')

$.ajax({
    type: 'GET',
    url: '/forum/list/',
    success: function(response) {
        console.log('Get Success: ', response)
        const data = response.data
        console.log(data)
        data.forEach(el => {
            threadBox.innerHTML += `
            <div class="card shadow-lg row-hover pos-relative px-3 mb-3 rounded-2 left-border">
                <div class="row pb-3 align-items-center">
                <div class="col-md-8 mb-3 mb-sm-0">
                   ${el.topic} <br>
                   ${el.description}
            </div>
        </div>
    </div>  `
        });
    },
    error: function(error) {
        console.log('Error: ', error);
    }
});

newTForm.addEventListener('submit', e => {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '',
        data: {
            'csrfmiddlewaretoken': csrf[0].value,
            'topic': topic.value,
            'description': description.value,
            'category': category.value,
        },
        success: function(response) {
            threadBox.insertAdjacentHTML('afterbegin', `
            <div class="card shadow-lg row-hover pos-relative px-3 mb-3 rounded-2 left-border">
                <div class="row pb-3 align-items-center">
                <div class="col-md-8 mb-3 mb-sm-0">
                   ${response.topic} <br>
                   ${response.description}
            </div>
        </div>
    </div>  `)
        },
        error: function(error) {
            console.log('Error: ', error);
        }
    });
});