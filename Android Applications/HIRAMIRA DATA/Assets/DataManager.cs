using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
using System.Net;
using uPLibrary.Networking.M2Mqtt;
using uPLibrary.Networking.M2Mqtt.Messages;
using uPLibrary.Networking.M2Mqtt.Utility;
using uPLibrary.Networking.M2Mqtt.Exceptions;
using System;

public class DataManager : MonoBehaviour {
    private MqttClient client;
    public InputField name, bedno, age, sex, diag, lam, lan;
    void Start () {
        name.text = PlayerPrefs.GetString("name", "");
        bedno.text = PlayerPrefs.GetString("bedno", "");
        age.text = PlayerPrefs.GetString("age", "");
        sex.text = PlayerPrefs.GetString("sex", "");
        diag.text = PlayerPrefs.GetString("diag", "");
        lam.text = PlayerPrefs.GetString("lam", "");
        lan.text = PlayerPrefs.GetString("lan", "");
        client = new MqttClient(IPAddress.Parse("10.177.7.168"), 1883, false, null);
        string clientId = Guid.NewGuid().ToString();
        client.Connect(clientId);

    }
    public void submit()
    {
        StartCoroutine(Upload());
    }
    IEnumerator Upload()
    {
        PlayerPrefs.SetString("name", name.text);
        PlayerPrefs.SetString("bedno", bedno.text);
        PlayerPrefs.SetString("age", age.text);
        PlayerPrefs.SetString("sex", sex.text);
        PlayerPrefs.SetString("diag", diag.text);
        PlayerPrefs.SetString("lam", lam.text);
        PlayerPrefs.SetString("lan", lan.text);
        WWWForm form = new WWWForm();

        form.AddField("name", name.text);
        form.AddField("bedno", bedno.text);
        form.AddField("age", age.text);
        form.AddField("sex", sex.text);
        form.AddField("diag", diag.text);
        form.AddField("lam", lam.text);
        form.AddField("lan", lan.text);
        UnityWebRequest www = UnityWebRequest.Post("http://10.177.7.168:5000/upload-data/", form);
        yield return www.SendWebRequest();

        if (www.isNetworkError || www.isHttpError)
        {
            Debug.Log(www.error);
        }
        else
        {
            client.Publish("data/"+bedno.text, System.Text.Encoding.UTF8.GetBytes(name.text+" | "+age.text + " | " +sex.text + " | " +diag.text + " | " +lam.text + " | " +lan.text), MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, true);
            SceneManager.LoadScene("ARscene");
        }
    }
}
