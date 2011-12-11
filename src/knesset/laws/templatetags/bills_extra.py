#encoding: utf-8
from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('laws/bill_full_name.html')
def bill_full_name(bill):
    return { 'bill': bill }

@register.inclusion_tag('laws/bill_list_item.html')
def bill_list_item(bill):
    return { 'bill': bill }

@register.inclusion_tag('laws/item_tags.html')
def item_tags(tags):
    return { 'tags': tags }

@register.inclusion_tag('laws/bill_inabox.html')
def bill_inabox(bill):
    """ TODO: firstX and not first3"""

#    CONVERT_TO_DISCUSSION_HEADERS = ('להעביר את הנושא'.decode('utf8'), 'העברת הנושא'.decode('utf8'))

#    discussion = False
#    for v in bill.pre_votes.all():
#        for h in CONVERT_TO_DISCUSSION_HEADERS:
#            if v.title.find(h)>=0: # converted to discussion
#                discussion = True
    bill_inabox_dict = dict({ 'MEDIA_URL' : settings.MEDIA_URL,
                 'bill': bill,
            'proposers_first3' : bill.proposers.all()[:3],
            'proposers_count_minus3' : bill.proposers.count() - 3})

    if bill.pre_votes.count() > 0:
        pre_vote_last = bill.pre_votes.all()[bill.pre_votes.count() - 1]
        pre_vote_dict = dict({'pre_vote_last' : pre_vote_last,
                              'pre_vote_time' : {'day' : pre_vote_last.time.day,
                               'month' : pre_vote_last.time.month,
                               'year' : pre_vote_last.time.year}})
        bill_inabox_dict = dict(bill_inabox_dict.items() + pre_vote_dict.items())

    # what is the real index? 0 is not the correct one
    return bill_inabox_dict