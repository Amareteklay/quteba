from django import template

register = template.Library()

@register.inclusion_tag('qforum/reply.html', takes_context=True)
def reply_tree(context):
    comment = context['comment']
    user = context['user']
    comment_form = context['comment_form']
    replies = comment.replies.all()
    return {"replies": replies, "user": user, "comment_form": comment_form}