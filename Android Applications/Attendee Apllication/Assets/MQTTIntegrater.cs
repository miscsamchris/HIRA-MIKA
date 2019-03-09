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

    public TMPro.TMP_Text t;
    private MqttClient client;
    public string heartbeat="65";

    // Use this for initialization
    void Start () {
        client = new MqttClient(IPAddress.Parse("10.177.7.168"), 1883, false, null);

        // register to message received 
        client.MqttMsgPublishReceived += client_MqttMsgPublishReceived;

        string clientId = Guid.NewGuid().ToString();
        client.Connect(clientId);

        // subscribe to the topic "/home/temperature" with QoS 2 
        client.Subscribe(new string[] { "heart" }, new byte[] { MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE });
    }
    void client_MqttMsgPublishReceived(object sender, MqttMsgPublishEventArgs e)
    {
        if (e.Topic=="heart")
        {
            heartbeat = System.Text.Encoding.UTF8.GetString(e.Message);
        }
    }
    // Update is called once per frame
    void Update () {
        t.text = heartbeat;
	}
}
