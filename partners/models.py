from django.db import models
from home.models import *
# from projects.models import Project
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import RegexValidator


class CommunityPartner (models.Model):
    TRUE_FALSE_CHOICES = (
        ('True', 'Yes'),
        ('False', 'No'),
    )

    CommunityPartnerName = models.CharField(max_length= 100)
    website_url = models.URLField(max_length= 100,blank=True)
    communitytype = models.ForeignKey('CommunityType', max_length=50, on_delete=models.SET_NULL,
                                      related_name='communitytype', null=True)
    k12_level =  models.CharField(max_length=20,null=False, blank=True)
    primary_mission = models.ForeignKey('home.MissionArea', on_delete=models.SET_NULL, related_name='primary_mission',
                                        null=True)
    secondary_mission = models.ForeignKey('home.MissionArea', on_delete=models.SET_NULL, related_name='second_mission',
                                          null=True)
    other = models.CharField(max_length=20, null=True, blank=True)
    address_line1 = models.CharField(max_length=1024,blank=True)
    address_line2 = models.CharField(max_length=1024, blank=True)
    country = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=25,blank=True)
    state = models.CharField(max_length=15,blank=True)
    Zip = models.CharField(max_length=10,blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True,null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True,null=True)
    active = models.BooleanField(default= True)
    weitz_cec_part = models.CharField(max_length=6 , choices= TRUE_FALSE_CHOICES, default= False )


    def __str__(self):
        return str(self.CommunityPartnerName)


class CommunityType (models.Model):

    community_type = models.CharField(max_length=50)

    def __str__(self):
        return str(self.community_type)

"""
class CommunityPartnerMission (models.Model):
    partner_name = models.ForeignKey(CommunityPartner, on_delete=models.CASCADE)
    mission_type = models.CharField(max_length=20)
    mission_code = models.ForeignKey('home.MissionArea', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.partner_name)
"""

class University (models.Model):
    college = models.CharField(max_length=50)
    department = models.CharField(max_length=30)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Course(models.Model):
    prefix = models.CharField(max_length=80)
    number = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    project_id = models.ForeignKey('projects.Project', on_delete=models.CASCADE)


# class CampusPartnerUser(models.Model):
#     campuspartner = models.ForeignKey('CampusPartner', on_delete=models.CASCADE)
#     user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)


class CampusPartner(models.Model):
    TRUE_FALSE_CHOICES = (
        ('True', 'Yes'),
        ('False', 'No'),
    )
    campus_partner_name = models.CharField(max_length=255)
    department_id = models.ForeignKey('University', on_delete=models.CASCADE)
    weitz_cec_part = models.CharField(max_length=6 , choices= TRUE_FALSE_CHOICES, default= False )
    campus_partner_user = models.ForeignKey


class CampusPartnerUser(models.Model):
    campuspartner = models.ForeignKey('CampusPartner', on_delete=models.CASCADE)
    #communitypartner = models.ForeignKey('CommunityPartner', on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE,)
    #emailid = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null = False)
    #email_id = models.ForeignKey('home.CampusPartnerContact', on_delete=models.CASCADE)


class CommunityPartnerUser(models.Model):
    #campuspartner = models.ForeignKey('CampusPartner', on_delete=models.CASCADE)
    communitypartner = models.ForeignKey('CommunityPartner', on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE,)
