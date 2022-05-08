from django import template

register = template.Library()

@register.inclusion_tag('qforum/reply.html')
def reply_tree(comment):
    replies = comment.replies.all()
    return {"replies": replies}