from django.test import TestCase
from qforum.forms import ThreadForm, CommentForm

class TestThreadForm(TestCase):
    def test_empty_form(self):
        form = ThreadForm()
        self.assertIn('topic', form.fields)
        self.assertIn('category', form.fields)
        self.assertIn('description', form.fields)
    
    def test_thread_form_category_field_label(self):
        form = ThreadForm()
        self.assertTrue(form.fields['category'].label is None or form.fields['category'].label == 'category')

    def test_thread_form_topic_field_label(self):
        form = ThreadForm()
        self.assertTrue(form.fields['topic'].label is None or form.fields['topic'].label == 'topic')


