from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^logout', views.logout),
    url(r'^login', views.login_page),
    url(r'^post/operate', views.post_operate),
    url(r'^post/star', views.post_star),
    url(r'^post/submit', views.post_submit),
    # url(r'^activity/attend', views.activity_attend),
    # url(r'^activity/detail', views.activity_detail),
    # url(r'^activity/list', views.activity_list),
    # url(r'^activity/operate', views.activity_operate),
    url(r'^club/profile/submit', views.club_profile_submit),
    url(r'^club/profile/get', views.club_profile_get),
    # url(r'^club/recruit/classroom/submit', views.recruit_classroom_apply),
    # url(r'^club/recruit/classroom/operate', views.recruit_classroom_operate),
    # url(r'^club/recruit/classroom/list', views.recruit_classroom_list),
    url(r'^user/profile/submit', views.userprofile_submit),
    url(r'^user/profile/get', views.userprofile_get),
    url(r'^club/member/add', views.club_member_add),
    url(r'^club/member/remove', views.club_member_remove),
    url(r'^club/member/list/confirmed', views.club_confirmed_member_list),
    url(r'^club/member/list/unconfirmed', views.club_unconfirmed_member_list),
    # url(r'^club/establish', views.club_establish),
    # url(r'^club/page', views.club_page),
    url(r'^club/attend', views.club_attend),
    url(r'^club/quit', views.club_quit),
    # url(r'^club/page/settings', views.club_page_setting),
    url(r'^post/list', views.post_list),
    url(r'^club/list', views.club_list),
    url(r'^club/show', views.club_show),
    #url(r'^club/file/download', views.club_list),
    #url(r'^cd/file/upload', views.cd_file_upload),
    url(r'^cd/file/download', views.club_list),
    url(r'^',views.index)
]
