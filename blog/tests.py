from django.test import TestCase
from django.shortcuts import reverse

from .models import blogPost
from django.contrib.auth.models import User


class blogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='morteza')
        cls.post1 = blogPost.objects.create(
            title='hello',
            text='text',
            auther=cls.user,
            status=blogPost.STATUS_CHOICES[0][0]
        )

        cls.post2 = blogPost.objects.create(
            title='hello2',
            text='text2',
            auther=cls.user,
            status=blogPost.STATUS_CHOICES[1][0]
        )

    def test_post_model_str(self):
        post = self.post1
        self.assertEqual(str(post), post.title)

    def test_post_detail(self):
        self.assertEqual(self.post1.title, 'hello')
        self.assertEqual(self.post1.text, 'text')

    def test_postListView(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_NamePost(self):
        response = self.client.get(reverse('post_blog'))
        self.assertEqual(response.status_code, 200)

    def test_content_blog(self):
        response = self.client.get(reverse('post_blog'))
        self.assertContains(response, self.post1.text)

    def test_detail_content_blog(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertContains(response, self.post1.text)

    def test_detail_name_blog(self):
        response = self.client.get(
            reverse('post_detail_blog', args=[self.post1.id]))
        self.assertContains(response, self.post1.text)

    def test_404_post_blog(self):
        response = self.client.get(
            reverse('post_detail_blog', args=[999]))
        self.assertEqual(response.status_code, 404)

    # --------------------------test draft ----------------------------
    def test_draft_not_show_blog(self):
        response = self.client.get(reverse('post_blog'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_post_create(self):
        response = self.client.post(reverse('add_post_blog'), {
            'title': 'test add post',
            'text': 'insert data',
            'auther': self.user.id,
            'status': 'pub',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(blogPost.objects.last().title, 'test add post')
        self.assertEqual(blogPost.objects.last().text, 'insert data')

    def test_post_edit(self):
        response = self.client.post(
            reverse('post_edit_blog', args=[self.post2.id]), {
                'title': 'test edit post',
                'text': 'edit data',
                'auther': self.post2.auther.id,
                'status': 'pub',
            })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(blogPost.objects.last().title, 'test edit post')
        self.assertEqual(blogPost.objects.last().text, 'edit data')

    def test_post_delete(self):
        response = self.client.post(
            reverse('post_delete_blog', args=[self.post2.id]))
        self.assertEqual(response.status_code, 302)
