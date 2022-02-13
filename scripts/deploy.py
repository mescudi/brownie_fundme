from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    deployMocks,
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENT,
)

DECIMALS = 18
STARTING_PRICE = 2000


def deploy_fund_me():
    account = get_account()

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deployMocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
