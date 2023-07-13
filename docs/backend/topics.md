---
label: MQTT Topics
order: 0
---
# MQTT Broker
The MQTT broker is used to send data from the simulator to the ingester and the frontend.
The broker used is [EMQX](https://www.emqx.io/) because it is open source and easy to use.

## Subscribe Topics
The MQTT topics used by the system are listed below.

| Topic                                      | Description                                                                                            | Payload                            |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------|------------------------------------|
| t/simulator/silos/<silos_id>/command/fill  | Fill the silo                                                                                          | `{"percentage": 100}`              |
| t/simulator/silos/<silos_id>/command/empty | Empty the silo                                                                                         | `{"percentage": 0}`                |
| t/simulator/silos/<silos_id>/command/start | Start the simulator                                                                                    | data serialized from DB            |
| t/simulator/silos/<silos_id>/command/stop  | Stop the simulator                                                                                     |                                    |
| t/simulator/silos/<silos_id>/command/idle  | Set the simulator in idle mode(level sensor does not change while other sensors continue to send data) |                                    |
| t/simulator/silos/<silos_id>/command/kill  | Kill the simulator                                                                                     | `{"kill": true, "id": <silos_id>}` |

## Publish Topics
| Topic                                            | Description                                                                                                                                                    |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| t/simulator/silos/<silos_id>/measurements/<slug> | Send the measurements of the silo identified by the <silos_id>. The slug can be `level`, `temperature`, `humidity`, `weight`, `pressure`, `filling_percentage` |
