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
slug = document.getElementById('id_slug')
description = document.getElementById('id_description')
category = document.getElementById('id_category')

const csrf = document.getElementsByName('csrfmiddlewaretoken')
const threadBox = document.getElementById('thread-box')
const url = window.location.href

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
                <img class="rounded-circle article-img profile-img" src="${el.profile}">
                <a class="text-black" href="#"> ${el.name}</a> <span class="op-6 text-muted">| ${el.created}</span>
                <h5 class="pt-3 px-3">
                    <a href="${url}${el.slug}" class="text-primary">${ el.topic}</a>
                </h5>
                <div class="px-3">
                    ${el.description}
                </div>
            </div>
            <div class="px-4">
                <span class="d-inline-block text-sm text-muted"> <i class="fa-solid fa-caret-up"></i>
                ${el.up_votes} </span>
                <span class="d-inline-block text-sm text-muted mx-3"> <i class="fa-solid fa-caret-down"></i>
                ${el.down_votes}  </span>
                <span class="d-inline-block text-sm text-muted mx-3"><i class="fa-solid fa-comments"></i>
                ${el.no_of_comments} </span>
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
                <img class="rounded-circle article-img profile-img" src="${response.profile}">
                <a class="text-black" href="#"> ${response.name}</a> <span class="op-6 text-muted">
                |${response.created} ago</span>
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
    </div> `);
            $('#addForumModal').modal('hide');
            newTForm.reset();
        },
        error: function(error) {
            console.log('Error: ', error);
        }
    });
});