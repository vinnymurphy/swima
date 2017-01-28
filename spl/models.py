from django.db import models

class StrokeLength(models.Model):
    """Stroke Length is a measurement of how much traction we are getting on each
    stroke. A stroke length that is "too short" is the equivalent of the car's
    wheels spinning in the mud – in terms of water it means we are pushing
    water around more than pushing our body forward. It shows us how much our
    arms are slipping backward through the water instead of our body slipping
    forward through the water."""
    'https://smoothstrokes.wordpress.com/2014/03/01/metrics-101-stroke-length/'

    # TODO: add user
    # SL = (LP – DG) / SC
    pool_length = models.IntegerField(default=25)
    glide_distance = models.IntegerField(
        help=('An average fitness swimmer Glide Distance may be around '
              '4 meters. A developed competitive swimmer may be '
              'around 5 meters or more.'),
        default=4)
    stroke_count = models.IntegerField(
        help=('After you push off and take that first underwater stroke '
              '(count that as stroke #0) count how many strokes it takes you '
              'to reach the other wall, without any extra glide when you are '
              'about to reach it. This will be your Stroke Count, or SC '
              '(aka SPL).'),
        default=18)
    wingspan = models.IntegerField(
        help=('The first objectively measurable feature of truly good '
              'freestyle technique is Stroke Length. By a great deal of data '
              'crunching and observation we estimate that a good freestyle '
              'stroke should be within 55% to 70% of a swimmer’s wingspan '
              '(or height, if you only know that measurement – it is '
              'approximately the same, give +/- 5%, and sufficient for '
              'most swimmers to calculate by).'))
