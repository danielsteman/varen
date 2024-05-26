import pytest

from varen.main import parse_weather_forecast_xml


@pytest.fixture
def data():
    return """<?xml version="1.0" encoding="UTF-8"?>
    <dataroot xmlns:od="urn:schemas-microsoft-com:officedata" generated="2024-05-26T18:06:07">
    <Middellange_x0020_en_x0020_lange_x0020_Termijn>
        <verwachting_meerdaagse>Wisselvallig met dagelijks regen- of onweersbuien. De temperaturen liggen overdag onder de 20°C.</verwachting_meerdaagse>
        <verwachting_lange_termijn_tekst>Een kans van rond de 40% op een overgang naar een iets minder wisselvallig weertype met maxima die geleidelijk naar rond normaal gaan. De kans op droger en warmer weerbeeld ligt rond de 20%.</verwachting_lange_termijn_tekst>
        <zonneschijnkans_dag1>30</zonneschijnkans_dag1>
        <neerslagkans_dag1>50</neerslagkans_dag1>
        <neerslaghoeveelheid_min_dag1>0</neerslaghoeveelheid_min_dag1>
        <neerslaghoeveelheid_max_dag1>0</neerslaghoeveelheid_max_dag1>
        <minimumtemperatuur_min_dag1>8</minimumtemperatuur_min_dag1>
        <minimumtemperatuur_max_dag1>12</minimumtemperatuur_max_dag1>
        <maximumtemperatuur_min_dag1>17</maximumtemperatuur_min_dag1>
        <maximumtemperatuur_max_dag1>20</maximumtemperatuur_max_dag1>
        <windrichting_dag1>ZW</windrichting_dag1>
        <windkracht_dag1>3</windkracht_dag1>
        <zonneschijnkans_dag2>30</zonneschijnkans_dag2>
        <neerslagkans_dag2>40</neerslagkans_dag2>
        <neerslaghoeveelheid_min_dag2>1</neerslaghoeveelheid_min_dag2>
        <neerslaghoeveelheid_max_dag2>1</neerslaghoeveelheid_max_dag2>
        <minimumtemperatuur_min_dag2>9</minimumtemperatuur_min_dag2>
        <minimumtemperatuur_max_dag2>10</minimumtemperatuur_max_dag2>
        <maximumtemperatuur_min_dag2>18</maximumtemperatuur_min_dag2>
        <maximumtemperatuur_max_dag2>19</maximumtemperatuur_max_dag2>
        <windrichting_dag2>W</windrichting_dag2>
        <windkracht_dag2>3</windkracht_dag2>
        <zonneschijnkans_dag3>30</zonneschijnkans_dag3>
        <neerslagkans_dag3>80</neerslagkans_dag3>
        <neerslaghoeveelheid_min_dag3>1</neerslaghoeveelheid_min_dag3>
        <neerslaghoeveelheid_max_dag3>1</neerslaghoeveelheid_max_dag3>
        <minimumtemperatuur_min_dag3>10</minimumtemperatuur_min_dag3>
        <minimumtemperatuur_max_dag3>12</minimumtemperatuur_max_dag3>
        <maximumtemperatuur_min_dag3>18</maximumtemperatuur_min_dag3>
        <maximumtemperatuur_max_dag3>20</maximumtemperatuur_max_dag3>
        <windrichting_dag3>ZW</windrichting_dag3>
        <windkracht_dag3>3</windkracht_dag3>
        <zonneschijnkans_dag4>20</zonneschijnkans_dag4>
        <neerslagkans_dag4>80</neerslagkans_dag4>
        <neerslaghoeveelheid_min_dag4>2</neerslaghoeveelheid_min_dag4>
        <neerslaghoeveelheid_max_dag4>2</neerslaghoeveelheid_max_dag4>
        <minimumtemperatuur_min_dag4>12</minimumtemperatuur_min_dag4>
        <minimumtemperatuur_max_dag4>14</minimumtemperatuur_max_dag4>
        <maximumtemperatuur_min_dag4>17</maximumtemperatuur_min_dag4>
        <maximumtemperatuur_max_dag4>20</maximumtemperatuur_max_dag4>
        <windrichting_dag4>W</windrichting_dag4>
        <windkracht_dag4>3</windkracht_dag4>
        <zonneschijnkans_dag5>20</zonneschijnkans_dag5>
        <neerslagkans_dag5>80</neerslagkans_dag5>
        <neerslaghoeveelheid_min_dag5>1</neerslaghoeveelheid_min_dag5>
        <neerslaghoeveelheid_max_dag5>1</neerslaghoeveelheid_max_dag5>
        <minimumtemperatuur_min_dag5>10</minimumtemperatuur_min_dag5>
        <minimumtemperatuur_max_dag5>12</minimumtemperatuur_max_dag5>
        <maximumtemperatuur_min_dag5>17</maximumtemperatuur_min_dag5>
        <maximumtemperatuur_max_dag5>19</maximumtemperatuur_max_dag5>
        <windrichting_dag5>W</windrichting_dag5>
        <windkracht_dag5>3</windkracht_dag5>
        <zonneschijnkans_dag6>20</zonneschijnkans_dag6>
        <neerslagkans_dag6>80</neerslagkans_dag6>
        <neerslaghoeveelheid_min_dag6>1</neerslaghoeveelheid_min_dag6>
        <neerslaghoeveelheid_max_dag6>1</neerslaghoeveelheid_max_dag6>
        <minimumtemperatuur_min_dag6>10</minimumtemperatuur_min_dag6>
        <minimumtemperatuur_max_dag6>12</minimumtemperatuur_max_dag6>
        <maximumtemperatuur_min_dag6>17</maximumtemperatuur_min_dag6>
        <maximumtemperatuur_max_dag6>20</maximumtemperatuur_max_dag6>
        <windrichting_dag6>NW</windrichting_dag6>
        <windkracht_dag6>3</windkracht_dag6>
        <norm_m1_dec1_tx>15.9</norm_m1_dec1_tx>
        <norm_m1_dec1_tn>7.3</norm_m1_dec1_tn>
        <norm_m1_dec1_ss>43</norm_m1_dec1_ss>
        <norm_m1_dec1_rh>17.6</norm_m1_dec1_rh>
        <norm_m1_dec2_tx>17.4</norm_m1_dec2_tx>
        <norm_m1_dec2_tn>8.4</norm_m1_dec2_tn>
        <norm_m1_dec2_ss>45</norm_m1_dec2_ss>
        <norm_m1_dec2_rh>17.9</norm_m1_dec2_rh>
        <norm_m1_dec3_tx>18</norm_m1_dec3_tx>
        <norm_m1_dec3_tn>9.2</norm_m1_dec3_tn>
        <norm_m1_dec3_ss>43</norm_m1_dec3_ss>
        <norm_m1_dec3_rh>21.3</norm_m1_dec3_rh>
        <norm_m2_dec1_tx>19.4</norm_m2_dec1_tx>
        <norm_m2_dec1_tn>10.6</norm_m2_dec1_tn>
        <norm_m2_dec1_ss>39</norm_m2_dec1_ss>
        <norm_m2_dec1_rh>26.2</norm_m2_dec1_rh>
        <norm_m2_dec2_tx>19.2</norm_m2_dec2_tx>
        <norm_m2_dec2_tn>10.8</norm_m2_dec2_tn>
        <norm_m2_dec2_ss>41</norm_m2_dec2_ss>
        <norm_m2_dec2_rh>16.9</norm_m2_dec2_rh>
        <norm_m2_dec3_tx>20.3</norm_m2_dec3_tx>
        <norm_m2_dec3_tn>11.7</norm_m2_dec3_tn>
        <norm_m2_dec3_ss>40</norm_m2_dec3_ss>
        <norm_m2_dec3_rh>21.9</norm_m2_dec3_rh>
        <dag-1_dd>25</dag-1_dd>
        <dag0_dd>26</dag0_dd>
        <dag1_dd>27</dag1_dd>
        <dag2_dd>28</dag2_dd>
        <dag3_dd>29</dag3_dd>
        <dag4_dd>30</dag4_dd>
        <dag5_dd>31</dag5_dd>
        <dag6_dd>01</dag6_dd>
        <dag7_dd>02</dag7_dd>
        <dag8_dd>03</dag8_dd>
        <dag9_dd>04</dag9_dd>
        <dag10_dd>05</dag10_dd>
        <dag-1_mm>05</dag-1_mm>
        <dag0_mm>05</dag0_mm>
        <dag1_mm>05</dag1_mm>
        <dag2_mm>05</dag2_mm>
        <dag3_mm>05</dag3_mm>
        <dag4_mm>05</dag4_mm>
        <dag5_mm>05</dag5_mm>
        <dag6_mm>06</dag6_mm>
        <dag7_mm>06</dag7_mm>
        <dag8_mm>06</dag8_mm>
        <dag9_mm>06</dag9_mm>
        <dag10_mm>06</dag10_mm>
        <dag-1_yy>24</dag-1_yy>
        <dag0_yy>24</dag0_yy>
        <dag1_yy>24</dag1_yy>
        <dag2_yy>24</dag2_yy>
        <dag3_yy>24</dag3_yy>
        <dag4_yy>24</dag4_yy>
        <dag5_yy>24</dag5_yy>
        <dag6_yy>24</dag6_yy>
        <dag7_yy>24</dag7_yy>
        <dag8_yy>24</dag8_yy>
        <dag9_yy>24</dag9_yy>
        <dag10_yy>24</dag10_yy>
        <dag-1_ddd>za</dag-1_ddd>
        <dag0_ddd>zo</dag0_ddd>
        <dag1_ddd>ma</dag1_ddd>
        <dag2_ddd>di</dag2_ddd>
        <dag3_ddd>wo</dag3_ddd>
        <dag4_ddd>do</dag4_ddd>
        <dag5_ddd>vr</dag5_ddd>
        <dag6_ddd>za</dag6_ddd>
        <dag7_ddd>zo</dag7_ddd>
        <dag8_ddd>ma</dag8_ddd>
        <dag9_ddd>di</dag9_ddd>
        <dag10_ddd>wo</dag10_ddd>
        <dag-1_dddd_dd_mmmm_yyyy>zaterdag 25 mei 2024</dag-1_dddd_dd_mmmm_yyyy>
        <dag0_dddd_dd_mmmm_yyyy>zondag 26 mei 2024</dag0_dddd_dd_mmmm_yyyy>
        <dag1_dddd_dd_mmmm_yyyy>maandag 27 mei 2024</dag1_dddd_dd_mmmm_yyyy>
        <dag2_dddd_dd_mmmm_yyyy>dinsdag 28 mei 2024</dag2_dddd_dd_mmmm_yyyy>
        <dag3_dddd_dd_mmmm_yyyy>woensdag 29 mei 2024</dag3_dddd_dd_mmmm_yyyy>
        <dag4_dddd_dd_mmmm_yyyy>donderdag 30 mei 2024</dag4_dddd_dd_mmmm_yyyy>
        <dag5_dddd_dd_mmmm_yyyy>vrijdag 31 mei 2024</dag5_dddd_dd_mmmm_yyyy>
        <dag6_dddd_dd_mmmm_yyyy>zaterdag 01 juni 2024</dag6_dddd_dd_mmmm_yyyy>
        <dag7_dddd_dd_mmmm_yyyy>zondag 02 juni 2024</dag7_dddd_dd_mmmm_yyyy>
        <dag8_dddd_dd_mmmm_yyyy>maandag 03 juni 2024</dag8_dddd_dd_mmmm_yyyy>
        <dag9_dddd_dd_mmmm_yyyy>dinsdag 04 juni 2024</dag9_dddd_dd_mmmm_yyyy>
        <dag10_dddd_dd_mmmm_yyyy>woensdag 05 juni 2024</dag10_dddd_dd_mmmm_yyyy>
        <dag-1_dddd_dd_mmmm>zaterdag 25 mei</dag-1_dddd_dd_mmmm>
        <dag0_dddd_dd_mmmm>zondag 26 mei</dag0_dddd_dd_mmmm>
        <dag1_dddd_dd_mmmm>maandag 27 mei</dag1_dddd_dd_mmmm>
        <dag2_dddd_dd_mmmm>dinsdag 28 mei</dag2_dddd_dd_mmmm>
        <dag3_dddd_dd_mmmm>woensdag 29 mei</dag3_dddd_dd_mmmm>
        <dag4_dddd_dd_mmmm>donderdag 30 mei</dag4_dddd_dd_mmmm>
        <dag5_dddd_dd_mmmm>vrijdag 31 mei</dag5_dddd_dd_mmmm>
        <dag6_dddd_dd_mmmm>zaterdag 01 juni</dag6_dddd_dd_mmmm>
        <dag7_dddd_dd_mmmm>zondag 02 juni</dag7_dddd_dd_mmmm>
        <dag8_dddd_dd_mmmm>maandag 03 juni</dag8_dddd_dd_mmmm>
        <dag9_dddd_dd_mmmm>dinsdag 04 juni</dag9_dddd_dd_mmmm>
        <dag10_dddd_dd_mmmm>woensdag 05 juni</dag10_dddd_dd_mmmm>
        <tijd_aanmaak>18.06</tijd_aanmaak>
    </Middellange_x0020_en_x0020_lange_x0020_Termijn>
    </dataroot>
    """


def test_parser(data):
    got = parse_weather_forecast_xml(data)
    want = {}
    assert want == got
