""" Value objects """
from datetime import datetime
from marshmallow import Schema, fields


class Venue(Schema):

    venue_name = fields.Str(default="南市川テニスガーデン", dump_only=True)
    venue_timezone = fields.Str(default="Asia/Tokyo", dump_only=True)


class SemiOpenSingles(Venue):

    match_type = fields.Str(default="男子シングルス", dump_only=True)
    level = fields.Str(default="セミオープン", dump_only=True)
    url = fields.Url(
        default="https://minamiichikawa.jp/tennis_tournament/pg407.html", dump_only=True)
    duration_in_hours = fields.Integer(default=4)


class AdvanceDoubles(Venue):

    match_type = fields.Str(default="男子ダブルス", dump_only=True)
    level = fields.Str(default="アドバンス", dump_only=True)
    url = fields.Url(
        default="https://minamiichikawa.jp/tennis_tournament/pg408.html", dump_only=True)
    duration_in_hours = fields.Integer(default=4)


class AdvanceMixDoubles(Venue):

    match_type = fields.Str(default="混合ダブルス", dump_only=True)
    level = fields.Str(default="アドバンス", dump_only=True)
    url = fields.Url(
        default="https://minamiichikawa.jp/tennis_tournament/pg409.html", dump_only=True)
    duration_in_hours = fields.Integer(default=4)
