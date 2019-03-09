using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using uPLibrary.Networking.M2Mqtt;
using uPLibrary.Networking.M2Mqtt.Messages;
using uPLibrary.Networking.M2Mqtt.Utility;
using System.Net;
using uPLibrary.Networking.M2Mqtt.Exceptions;
using System;

public class MQTTIntegrater : MonoBehaviour {

    public TMPro.TMP_Text hb,bp,t,name,bedno,age,sex,diag,lam,lan;
    private MqttClient client;
    public GameObject a;
    private string heartbeat="65",BP="120",T="98.2",BIN="",NIN = "", AIN = "", SIN = "", DIN = "", LAMIN = "", LANIN = "";

    // Use this for initialization
    void Start () {
        client = new MqttClient(IPAddress.Parse("10.177.7.168"), 1883, false, null);

        // register to message received 
        client.MqttMsgPublishReceived += client_MqttMsgPublishReceived;

        string clientId = Guid.NewGuid().ToString();
        client.Connect(clientId);

        // subscribe to the topic "/home/temperature" with QoS 2 ,"bp","temp","data/"+a.name
        client.Subscribe(new string[] { "heart" }, new byte[] { MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE });
        client.Subscribe(new string[] { "bp" }, new byte[] { MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE });
        client.Subscribe(new string[] { "temp" }, new byte[] { MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE });
        client.Subscribe(new string[] { "data/" + a.name }, new byte[] { MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE });

    }
    void client_MqttMsgPublishReceived(object sender, MqttMsgPublishEventArgs e)
    {
        if (e.Topic=="heart")
        {
            heartbeat = System.Text.Encoding.UTF8.GetString(e.Message);
        }
        if (e.Topic == "bp")
        {
            BP = System.Text.Encoding.UTF8.GetString(e.Message);
        }
        if (e.Topic == "temp")
        {
            T = System.Text.Encoding.UTF8.GetString(e.Message);
        }
        if (e.Topic == "data/" + a.name)
        {
            string[] arr = System.Text.Encoding.UTF8.GetString(e.Message).Split('|');
            BIN = a.name;
            NIN = arr[0];
            AIN = arr[1];
            SIN = arr[2];
            DIN = arr[3];
            LAMIN = arr[4];
            LANIN = arr[5];
        }
    }
    // Update is called once per frame
    void Update () {
        hb.text = heartbeat;
        bp.text = BP;
        t.text = T;
        bedno.text = BIN;
        name.text = NIN;
        age.text = AIN;
        sex.text = SIN;
        diag.text = DIN;
        lam.text = LAMIN;
        lan.text = LANIN;
	}
}
