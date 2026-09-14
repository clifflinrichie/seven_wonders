from src.models.card import Card
from src.models.resource_bundle import ResourceBundle

from src.effects.resource_effect import ResourceEffect
from src.effects.point_effect import PointEffect
from src.effects.coin_effect import CoinEffect
from src.effects.trade_effect import TradeEffect
from src.effects.military_effect import MilitaryEffect

from src.constants.color import Color
from src.constants.resource import Resource
from src.constants.directions import Directions

from collections import Counter


def generate_cards():
    #######
    ## ACT 1
    #######

    # Common Resources
    lumber_yard = Card(name="lumber yard", 
                        cost=ResourceBundle(), 
                        age=1, 
                        color=Color.brown, 
                        effects=[ResourceEffect(ResourceBundle(wood=1))],
                        quantity_by_player_count=Counter({3: 1, 4: 2}))
    stone_pit = Card(name="stone pit", 
                        cost=ResourceBundle(), 
                        age=1, 
                        color=Color.brown, 
                        effects=[ResourceEffect(ResourceBundle(stone=1))],
                        quantity_by_player_count=Counter({3: 1, 5: 2}))
    clay_pool = Card(name="clay pool", 
                        cost=ResourceBundle(), 
                        age=1, 
                        color=Color.brown,
                        effects=[ResourceEffect(ResourceBundle(clay=1))],
                        quantity_by_player_count=Counter({3: 1, 5: 2}))
    ore_vein = Card(name="ore vein", 
                        cost=ResourceBundle(), 
                        age=1, 
                        color=Color.brown,
                        effects=[ResourceEffect(ResourceBundle(ore=1))],
                        quantity_by_player_count=Counter({3: 1, 4: 2}))
    tree_farm = Card(name="tree farm", 
                        cost=ResourceBundle(coin=1), 
                        age=1, 
                        color=Color.brown,
                        effects=[ResourceEffect(ResourceBundle(wood=1, clay=1))],
                        quantity_by_player_count=Counter({6: 1}))
    excavation = Card(name="excavation", 
                        cost=ResourceBundle(coin=1), 
                        age=1, 
                        color=Color.brown,
                        effects=[ResourceEffect(ResourceBundle(stone=1, clay=1))],
                        quantity_by_player_count=Counter({4: 1}))
    clay_pit = Card(name="clay pit", 
                        cost=ResourceBundle(coin=1), 
                        age=1, 
                        color=Color.brown,
                        effects=[ResourceEffect(ResourceBundle(ore=1, clay=1))],
                        quantity_by_player_count=Counter({3: 1}))
    timber_yard = Card(name="timber yard", 
                        cost=ResourceBundle(coin=1), 
                        age=1, 
                        color=Color.brown,
                        effects=[ResourceEffect(ResourceBundle(wood=1, stone=1))],
                        quantity_by_player_count=Counter({3: 1}))
    forest_cave = Card(name="forest cave", 
                        cost=ResourceBundle(coin=1), 
                        age=1, 
                        color=Color.brown,
                        effects=[ResourceEffect(ResourceBundle(wood=1, ore=1))],
                        quantity_by_player_count=Counter({5: 1}))
    mine = Card(name="mine", 
                        cost=ResourceBundle(coin=1), 
                        age=1, 
                        color=Color.brown,
                        effects=[ResourceEffect(ResourceBundle(stone=1, ore=1))],
                        quantity_by_player_count=Counter({6: 1}))

    # Rare Resources
    press = Card(name="press", 
                    cost=ResourceBundle(), 
                    age=1, 
                    color=Color.gray,
                    effects=[ResourceEffect(ResourceBundle(press=1))],
                    quantity_by_player_count=Counter({3: 1, 6: 2}))
    glassworks = Card(name="glassworks", 
                    cost=ResourceBundle(), 
                    age=1, 
                    color=Color.gray,
                    effects=[ResourceEffect(ResourceBundle(glassworks=1))],
                    quantity_by_player_count=Counter({3: 1, 6: 2}))
    loom = Card(name="loom", 
                    cost=ResourceBundle(), 
                    age=1, 
                    color=Color.gray,
                    effects=[ResourceEffect(ResourceBundle(loom=1))],
                    quantity_by_player_count=Counter({3: 1, 6: 2}))


    # Civil Buildings
    well = Card(name="well", 
                    cost=ResourceBundle(), 
                    age=1, 
                    color=Color.blue,
                    effects=[PointEffect(points=3)],
                    quantity_by_player_count=Counter({4: 1, 7: 2}))
    baths = Card(name="baths", 
                        cost=ResourceBundle(), 
                        age=1, 
                        color=Color.blue,
                        effects=[PointEffect(points=3)],
                        quantity_by_player_count=Counter({3: 1, 7: 2}))
    altar = Card(name="altar", 
                        cost=ResourceBundle(), 
                        age=1, 
                        color=Color.blue,
                        effects=[PointEffect(points=3)],
                        quantity_by_player_count=Counter({3: 1, 5: 2}))
    theater = Card(name="theater", 
                        cost=ResourceBundle(), 
                        age=1, 
                        color=Color.blue,
                        effects=[PointEffect(points=3)],
                        quantity_by_player_count=Counter({3: 1, 6: 2}))


    # Commercial Buildings
    common_resources = [Resource.wood, Resource.clay, Resource.ore, Resource.stone]
    rare_resources = [Resource.glassworks, Resource.loom, Resource.press]

    tavern = Card(name="tavern", 
                        cost=ResourceBundle(), 
                        age=1, 
                        color=Color.yellow,
                        effects=[CoinEffect(coins=5)],
                        quantity_by_player_count=Counter({4: 1, 5: 2, 7: 3}))
    marketplace = Card(name="marketplace",
                        cost=ResourceBundle(), 
                        age=1, 
                        color=Color.yellow,
                        effects=[TradeEffect(resources=rare_resources, directions=[Directions.east, Directions.west])],
                        quantity_by_player_count=Counter({3: 1, 6: 2}))
    west_trading_post = Card(name="west trading post",
                        cost=ResourceBundle(), 
                        age=1, 
                        color=Color.yellow,
                        effects=[TradeEffect(resources=common_resources, directions=[Directions.west])],
                        quantity_by_player_count=Counter({3: 1, 7: 2}))
    east_trading_post = Card(name="east trading post",
                        cost=ResourceBundle(), 
                        age=1, 
                        color=Color.yellow,
                        effects=[TradeEffect(resources=common_resources, directions=[Directions.east])],
                        quantity_by_player_count=Counter({3: 1, 7: 2}))

    # Military Buildings
    stockade = Card(name="stockade",
                        cost=ResourceBundle(wood=1), 
                        age=1, 
                        color=Color.red,
                        effects=[MilitaryEffect(war=1, directions=[Directions.east, Directions.west])],
                        quantity_by_player_count=Counter({3: 1, 7: 2}))
    barracks = Card(name="barracks",
                        cost=ResourceBundle(ore=1), 
                        age=1, 
                        color=Color.red,
                        effects=[MilitaryEffect(war=1, directions=[Directions.east, Directions.west])],
                        quantity_by_player_count=Counter({3: 1, 5: 2}))
    guard_tower = Card(name="guard tower",
                        cost=ResourceBundle(clay=1), 
                        age=1, 
                        color=Color.red,
                        effects=[MilitaryEffect(war=1, directions=[Directions.east, Directions.west])],
                        quantity_by_player_count=Counter({3: 1, 4: 2}))

    # Science Buildings
    apothecary = Card(name="apothecary",
                        cost=ResourceBundle(loom=1), 
                        age=1, 
                        color=Color.green,
                        effects=[ResourceEffect(ResourceBundle(compass=1))],
                        quantity_by_player_count=Counter({3: 1, 5: 2}))
    workshop = Card(name="workshop",
                        cost=ResourceBundle(glassworks=1), 
                        age=1, 
                        color=Color.green,
                        effects=[ResourceEffect(ResourceBundle(wheel=1))],
                        quantity_by_player_count=Counter({3: 1, 7: 2}))
    scriptorium = Card(name="scriptorium",
                        cost=ResourceBundle(press=1), 
                        age=1, 
                        color=Color.green,
                        effects=[ResourceEffect(ResourceBundle(tablet=1))],
                        quantity_by_player_count=Counter({3: 1, 4: 2}))

    all_cards = [
        lumber_yard,
        stone_pit,
        clay_pool,
        ore_vein,
        tree_farm,
        excavation,
        clay_pit,
        timber_yard,
        forest_cave,
        mine,
        press,
        glassworks,
        loom,
        well,
        baths,
        altar,
        theater,
        tavern,
        marketplace,
        west_trading_post,
        east_trading_post,
        stockade,
        barracks,
        guard_tower,
        apothecary,
        workshop,
        scriptorium,
    ]
    return all_cards