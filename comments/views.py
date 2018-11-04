from django.http import JsonResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.template.loader import render_to_string

from videos.models import Video
from .models import Comment


class SubmitCommentAjax(LoginRequiredMixin, View):
    """
    采用AJax进行提交书评,
    前提条件：用户已登录和POST方式
    """
    def post(self, request):
        video_id = request.POST.get('vid', None)
        parent_id = request.POST.get('pid', None)
        content = request.POST.get('content', None)
        if video_id and parent_id and content:
            try:
                video = Video.objects.get(id=int(video_id))
                parent = (Comment.objects.get(id=int(parent_id)) if int(parent_id) > 0 else None)
                new_comment = Comment(user=request.user, video=video, parent=parent, content=content)
                new_comment.save()
                cmt_html = self.get_comment_html(request=request, video=video, new_comment=new_comment)
                return JsonResponse({'msg': 'ok', 'cmt': cmt_html})
            except (Video.DoesNotExist, Comment.DoesNotExist, BaseException) as e:
                print("书评异常信息:{0}".format(e))
                return JsonResponse({'msg': 'ko'})
        return JsonResponse({'msg': 'ko'})

    @staticmethod
    def get_comment_html(request, video, new_comment):
        cmt_html = render_to_string('comment-item.html',
                                    context={'comment': new_comment, 'video': video},
                                    request=request)
        return cmt_html


class LikeCommentAjax(LoginRequiredMixin, View):
    """
    采用Ajax进行喜欢书评操作
    允许条件: 用户已登录和只能通过post方式提交
    """
    def post(self, request):
        comment_id = request.POST.get('bid', None)
        action = request.POST.get('action', None)
        if comment_id and action:
            try:
                comment = Comment.objects.get(id=comment_id)
                if action == 'like':
                    comment.like_user.add(request.user)
                else:
                    comment.like_user.remove(request.user)
                return JsonResponse({'msg': 'ok'})
            except Comment.DoesNotExist:
                return JsonResponse({'msg': 'ko'})
        return JsonResponse({'msg': 'ko'})


class DeleteCommentAJax(LoginRequiredMixin, View):
    """
    采用Ajax进行删除评论操作
    允许条件: 用户已登录、只能删除自己的评论，只能通过post方式提交
    值得注意的是：如果删除的评论有回复的话，也一并会删除
    """
    def post(self, request):
        comment_id = request.POST.get('bid', None)
        if comment_id:
            try:
                comment = Comment.objects.get(id=int(comment_id))
                check_is_comment_user(request, comment)
                comment.delete()
                return JsonResponse({'msg': 'ok'})
            except Comment.DoesNotExist:
                return JsonResponse({'msg': 'ko'})
        return JsonResponse({'msg': 'ko'})


def check_is_comment_user(request, comment):
    """
    检查当前请求者是否为comment的user
    :param request:
    :param comment: 要检查的评论
    :return: 无
    """
    if request.user != comment.user:
        raise Http404



