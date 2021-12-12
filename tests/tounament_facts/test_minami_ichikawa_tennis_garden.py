from tournaments.tournament_facts_spec import Venue, SemiOpenSingles, AdvanceDoubles, AdvanceMixDoubles


def test_venue_success():
    result = Venue().dump({})

    assert result['venue_name_jpn'] == '南市川テニスガーデン'


def test_semi_open_singles_success():
    result = SemiOpenSingles().dump({})

    assert result['venue_name_jpn'] == '南市川テニスガーデン'
    assert result['match_type_jpn'] == '男子シングルス'
    assert result['level_jpn'] == 'セミオープン'
    assert result['url'] == 'https://minamiichikawa.jp/tennis_tournament/pg407.html'


def test_advance_doubles_success():
    result = AdvanceDoubles().dump({})

    assert result['venue_name_jpn'] == '南市川テニスガーデン'
    assert result['match_type_jpn'] == '男子ダブルス'
    assert result['level_jpn'] == 'アドバンス'
    assert result['url'] == 'https://minamiichikawa.jp/tennis_tournament/pg408.html'


def test_mix_doubles_success():
    result = AdvanceDoubles().dump({})

    assert result['venue_name_jpn'] == '南市川テニスガーデン'
    assert result['match_type_jpn'] == '混合ダブルス'
    assert result['level_jpn'] == 'アドバンス'
    assert result['url'] == 'https://minamiichikawa.jp/tennis_tournament/pg408.html'
