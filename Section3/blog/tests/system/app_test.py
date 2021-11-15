from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post


class AppTest(TestCase):
    # app.py에 있는 모든 함수들을 호출해나가면서 실행.
    # 이 파일이 왜 system directory냐 하면은, app에 있는 함수들을 이용해, 객체의 내부 객체까지 불러오기 때문.
    # 객체 여러개를 확인할 떄는 integration test test

    def setUp(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')
            app.menu()

            self.assertIsNotNone(app.blogs['Test Create Blog'])

    def test_print_blog(self):

        with patch('builtins.print') as mocked_print:
            app.print_blog()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')

    def test_print_input(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_pirnt_blogs(self):
        with patch('app.print_blog') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_ask_create_blog(self):
        # 적당히 만들고, Test라는 블로그가 존재하는 것을 확인.
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', "Test Author")
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):
        blog = app.blogs['Test']
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(blog)

    def test_print_posts(self):
        blog = app.blogs['Test']
        blog.create_post('Test Post', 'Test Content')

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('Post title', 'Post content')
        expected_post = '''
    --- Post title ---
    
    Post content
    
    '''
        with patch('builtins.print') as mocked_print:
            app.print_post(post)

            mocked_print.assert_called_with(expected_post)

    def test_ask_create_post(self):
        blog = app.blogs['Test']

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', "Test title", 'Test Content')
            app.ask_create_post()

            self.assertEqual(blog.posts[0].title, 'Test title')
            self.assertEqual(blog.posts[0].content, 'Test Content')
