from tournaments.tournament_facts import Venue, SemiOpenSingles, AdvanceDoubles, AdvanceMixDoubles


def test_venue_success():
    result = Venue().dump({})

    assert result['venue_name'] == '南市川テニスガーデン'


def test_semi_open_singles_success():
    result = SemiOpenSingles().dump({})

    assert result['venue_name'] == '南市川テニスガーデン'
    assert result['match_type'] == '男子シングルス'
    assert result['level'] == 'セミオープン'
    assert result['url'] == 'https://minamiichikawa.jp/tennis_tournament/pg407.html'


def test_advance_doubles_success():
    result = AdvanceDoubles().dump({})

    assert result['venue_name'] == '南市川テニスガーデン'
    assert result['match_type'] == '男子ダブルス'
    assert result['level'] == 'アドバンス'
    assert result['url'] == 'https://minamiichikawa.jp/tennis_tournament/pg408.html'


def test_mix_doubles_success():
    result = AdvanceDoubles().dump({})

    assert result['venue_name'] == '南市川テニスガーデン'
    assert result['match_type'] == '混合ダブルス'
    assert result['level'] == 'アドバンス'
    assert result['url'] == 'https://minamiichikawa.jp/tennis_tournament/pg408.html'
