from django.contrib.auth.models import User
from django.db import models


class StrokeLength(models.Model):
    """Stroke Length is a measurement of how much traction we are getting on each
    stroke. A stroke length that is "too short" is the equivalent of the car's
    wheels spinning in the mud – in terms of water it means we are pushing
    water around more than pushing our body forward. It shows us how much our
    arms are slipping backward through the water instead of our body slipping
    forward through the water."""
    'https://smoothstrokes.wordpress.com/2014/03/01/metrics-101-stroke-length/'

    user = models.ForeignKey(User, related_name='User', null=True)
    today = models.DateField()
    pool_length = models.PositiveSmallIntegerField(
        help_text='In yards', default=25)
    glide_distance = models.PositiveSmallIntegerField(
        help_text='In yards', default=5)
    stroke_count = models.PositiveSmallIntegerField(
        help_text='Number of strokes per length of pool',
        default=15)
    wingspan = models.PositiveSmallIntegerField(
        help_text='Inches Tall', default=68)

    def __str__(self):
        return '%s stroke length on %s' % (self.user, self.today)
