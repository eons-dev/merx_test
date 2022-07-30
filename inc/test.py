import os
import logging
from emi import Merx, Epitome

class test(Merx):
    def __init__(this, name="Test"):
        super().__init__(name)

        this.gotAllTomes = True

    # Required Merx method. See that class for details.
    def Transaction(this):
        logging.info(f"Tomes: {this.tomes}")
        logging.info(f"Paths: {this.paths}")
        logging.info(f"Catalog: {this.catalog}")

        for tome in this.tomes:
            epitome = this.GetTome(tome)
            if (epitome.path is None):
                this.gotAllTomes = False
            else:
                if (epitome.installed_at is None or not len(epitome.installed_at)):
                    epitome.installed_at = "NOT INSTALLED"
                if (epitome.additional_notes is None or not len(epitome.additional_notes)):
                    epitome.additional_notes="Test Retrieval Successful"
                this.catalog.add(epitome)

    # Required Merx method. See that class for details.
    def DidTransactionSucceed(this):
        return this.gotAllTomes

    # Required Merx method. See that class for details.
    def Rollback(this):
        super().Rollback()

    # Required Merx method. See that class for details.
    def DidRollbackSucceed(this):
        return True