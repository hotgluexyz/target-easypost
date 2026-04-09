from target_easypost.client import EasypostStream


class ShipmentSink(EasypostStream):

    name = "shipments"
    endpoint = "/shipments"

    def upsert_record(self, record: dict, context: dict):
        endpoint = f"/{self.name}"
        method = "POST"

        response = self.request_api(method, endpoint, request_data=record)
        res_json = response.json()
        id = res_json.get("id")
        state_updates = {}

        # buy a label
        # choose first option for now
        rates = res_json.get("rates")
        if not rates:
            raise ValueError("No rates found for shipment")
        first_rate = rates[0]
        buy_label_payload = {"rate": {"id": first_rate.get("id")}}
        self.request_api("POST", f"{self.endpoint}/{id}/buy", request_data=buy_label_payload)

        return id, response.ok, state_updates
    
