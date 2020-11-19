Bill of Materials
-----------------

+-----------------------------------------------------+----------+------------+-------------+------------------------------------------------------------------------------------------------------+
| Part                                                | Quantity | Unit Price | Total Price | Example Link                                                                                         |
+=====================================================+==========+============+=============+======================================================================================================+
| L298 Motor Driver (Dual H-Bridge DC Driver)         | 1        | ~$5.99     | $5.99       | `here <https://www.amazon.com/Controller-H-Bridge-Stepper-Mega2560-Duemilanove/dp/B01CC8XI60>`_      |
+-----------------------------------------------------+----------+------------+-------------+------------------------------------------------------------------------------------------------------+
| Raspberry Pi 3 Model B Board                        | 1        | ~$32.00    | $32.00      | `here <https://www.amazon.com/Raspberry-Pi-MS-004-00000024-Model-Board/dp/B01LPLPBS8>`_              |
+-----------------------------------------------------+----------+------------+-------------+------------------------------------------------------------------------------------------------------+
| Jumper Wire Kit having (M-F, M-M, and F-F is handy) | 1        | ~$5.00     | $5.00       | `here <https://www.amazon.com/EDGELEC-Breadboard-Optional-Assorted-Multicolored/dp/B07GD2BWPY>`_     |
+-----------------------------------------------------+----------+------------+-------------+------------------------------------------------------------------------------------------------------+
| Generic Roomba                                      | 1        | ~$30.00    | $30.00      | `here <https://www.ebay.com/itm/IRobot-Roomba-w-Charger/264939929657>`_                              |
+-----------------------------------------------------+----------+------------+-------------+------------------------------------------------------------------------------------------------------+
| 32GB microSDHC Memory Card                          | 1        | ~$7.49     | $7.49       | `here <https://www.amazon.com/Samsung-MicroSDHC-Adapter-MB-ME32GA-AM/dp/B06XWN9Q99>`_                |
+-----------------------------------------------------+----------+------------+-------------+------------------------------------------------------------------------------------------------------+
| 14-18vDC Lithium Polymer Battery Pack               | 1        | ~$15.99    | $15.99      | `here <https://www.amazon.com/1500mAh-POVWAY-Compatible-Airplane-Helicopter/dp/B07TT5BPCB>`_         |
+-----------------------------------------------------+----------+------------+-------------+------------------------------------------------------------------------------------------------------+
| 14-18vDC Lithium Polymer Battery Charger            | 1        | ~$37.99    | $37.99      | `here <https://www.amazon.com/Balance-Charger-Battery-Discharger-Supply/dp/B07Y8KG2PT>`_             |
+-----------------------------------------------------+----------+------------+-------------+------------------------------------------------------------------------------------------------------+
| XT90 Battery Connector Lead Wires/Pigtail           | 1        | ~$7.99     | $7.99       | `here <https://www.amazon.com/Amass-Connectors-Female-Silicone-Battery/dp/B084VK7N9D>`_              |
+-----------------------------------------------------+----------+------------+-------------+------------------------------------------------------------------------------------------------------+
| Lever Nuts Wire Connection Pack (28pc)              | 1        | ~$18.95    | $18.95      | `here <https://www.amazon.com/Wago-Lever-Nut-Assortment-Pocket-Pack/dp/B01N0LRTXZ>`_                 |
+-----------------------------------------------------+----------+------------+-------------+------------------------------------------------------------------------------------------------------+
| Limit Switch (Momentary, Hinge) (10pc)              | 1        | ~$6.99     | $6.99       | `here <https://www.amazon.com/URBESTAC-Momentary-Hinge-Roller-Switches/dp/B00MFRMFS6>`_              |
+-----------------------------------------------------+----------+------------+-------------+------------------------------------------------------------------------------------------------------+
| JBL CLIP 3 Portable Speaker                         | 1        | ~$39.95    | $39.95      | `here <https://www.amazon.com/JBL-Waterproof-Portable-Bluetooth-Speaker/dp/B07Q6ZWMLR>`_             |
+-----------------------------------------------------+----------+------------+-------------+------------------------------------------------------------------------------------------------------+
| Small USB Battery Bank (5vDC over USB)              | 1        | ~$19.99    | $19.99      | `here <https://www.amazon.com/Anker-PowerCore-Lipstick-Sized-Compatible-Smartphones/dp/B005X1Y7I2>`_ |
+-----------------------------------------------------+----------+------------+-------------+------------------------------------------------------------------------------------------------------+
| Momentary Push Button (Low Voltage)                 | 1        | ~$5.79     | $5.79       | `here <https://www.amazon.com/MCIGICM-Momentary-Button-Switch-Normal/dp/B07XXLHLT6>`_                |
+-----------------------------------------------------+----------+------------+-------------+------------------------------------------------------------------------------------------------------+
| Sullins Connector Solutions:RBB06DHHN               | 1        | ~$-.--     | $-.--       | Not available                                                                                        |
+-----------------------------------------------------+----------+------------+-------------+------------------------------------------------------------------------------------------------------+

The BOM is provided for your convenience. Please note that parts availability varies wildly, so any links provided might not still have active products. Consider getting some of your parts used. For your Roomba, only the motors need to be functional.

You need three separate battery packs: 1x5vDC, 1x14-18vDC, and one integrated into your speaker. If your battery pack is 18vDC, then you can use it, but you can also get a 18vDC LiPO battery and charger. The 18vDC battery is only used to drive the motors. The 5vDC battery pack should only be used to power the Raspberry Pi. You should get a small enough battery pack so it fits in the casing easily. Large banks are difficult to work with in the confined space of a Roomba.

During testing, consider using a bench power supply set to the target voltage of your battery pack, that way, you don't have to continuously charge the battery pack. Pick up another pack of XT90 leads and some primary wire.
