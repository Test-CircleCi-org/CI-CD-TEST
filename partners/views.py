from django.forms import formset_factory
from .forms import CampusPartnerForm, CampusPartnerContactForm, CampusPartnerFormProfile
from django.shortcuts import render
from .models import CampusPartner as CampusPartnerModel
from home.models import Contact as ContactModel, Contact
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory, modelformset_factory
from django.template import context
from partners.models import CampusPartner
from .forms import CampusPartnerForm, CampusPartnerContactForm

from django.shortcuts import render, redirect


def registerCampusPartner(request):
    ContactFormset = modelformset_factory(Contact, extra=1, form=CampusPartnerContactForm)
    if request.method == 'POST':
        campus_partner_form = CampusPartnerForm(request.POST )

        formset = ContactFormset(request.POST or None)

        if campus_partner_form.is_valid() and formset.is_valid():
                campus_partner = campus_partner_form.save()
                contacts = formset.save(commit=False)
                print(contacts)
                for contact in contacts:
                 contact.campus_partner = campus_partner
                 contact.save()
                 print(contact)
                return render(request, 'home/community_partner_register_done.html')

    else:
        campus_partner_form = CampusPartnerForm()
        formset = ContactFormset(queryset=Contact.objects.none())
    return render(request,
                  'registration/campus_partner_register.html',
                  {'campus_partner_form': campus_partner_form, 'formset': formset})


def registerCampusPartnerProfile(request):
  campus_partner_form = CampusPartnerFormProfile(request.POST or None)
  # We should get the partner by some unique ID directly based on the login information
  # current_campus_partner = CampusPartnerModel.objects.get(name="unique name")
  # Use try catch for using .get
  current_campus_partner = CampusPartnerModel.objects.all()[0]
  campus_partner_name = current_campus_partner.name
  college = current_campus_partner.college
  department = current_campus_partner.department
  # # Contact details from Contact Model
  # # We should use objects.get(campus_partner=current_campus_partner)
  # # as it gets the unqiue object mapping result in try catch. 
  
  try:
    partner_contact = ContactModel.objects.get(
      campus_partner=current_campus_partner
    )
    first_name = partner_contact.first_name
    last_name = partner_contact.last_name
    email = partner_contact.email_id
  except ContactModel.DoesNotExist:
    first_name = None
    last_name = None
    email = None
  return render(request,
                  'home/campus_partner_profile.html', {
                    'campus_partner_name': campus_partner_name,
                    'college': college,
                    'department': department,
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email               
                  })  