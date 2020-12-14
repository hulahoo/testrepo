from .models import Category, Post
from django.views.generic import ListView


class IndexPage(ListView):
    """главная страница"""
    model = Category
    template_name = 'mainapp/index_page.html'
    context_object_name = 'index-page'


    def get_queryset(self):
        """переназначение родительского метода """
        queryset = super().get_queryset()
        category_slug = self.request.GET.get('category')
        if category_slug is not None:
            queryset = queryset.filter(category_id=category_slug)
        return queryset

class PostListView(ListView):
    """листинг постов"""
    model = Post
    template_name = 'mainapp/index_app.html'
    context_object_name = 'index-page'

    def get_queryset(self):
        """переназначение родительского метода """
        queryset = super().get_queryset()
        category_slug = self.request.GET.get('category')
        if category_slug is not None:
            queryset = queryset.filter(category_id=category_slug)
        return queryset


# class PostDetailView(DetailView):
#     """детали поста"""
#     model = Post
#     # template_name = 'blog/post_details.html'
#     # context_object_name = 'post'
#
#
# class ContextMixin:
#     """Мы определяем один метод который нужен для всех классов"""
#     def get_context_data(self, *args, **kwargs):
#         """придаем логику в метод миксина"""
#         context = super().get_context_data(*args, **kwargs)
#         context['post_form'] = self.get_form(self.get_form_class())
#         return context

#
# class AddPostView(ContextMixin,CreateView):
#     """добавление поста"""
#     model = Post
#     # template_name = 'blog/add_post.html'
#     # form_class = AddPost
#
#     def form_valid(self, form):
#         """выполняется в том случае если все правильно"""
#         post = form.save()
#         return redirect(post.get_absolute_url())

#
# class UpdatePostView(ContextMixin, UpdateView):
#     """изменение поста"""
#     model = Post
#     template_name = 'blog/post_update.html'
#     form_class = EditPost
#     context_object_name = 'post'
#
#
# class DeletePostView(DeleteView):
#     """удаление поста"""
#     model = Post
#     template_name = 'blog/post_delete.html'
#     success_url = reverse_lazy('index-page')
