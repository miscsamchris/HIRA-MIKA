using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class DataManager : MonoBehaviour {

    public InputField name, bedno, age, sex, diag, lam, lan;
    void Start () {
        name.text = PlayerPrefs.GetString("name", "");
        bedno.text = PlayerPrefs.GetString("bedno", "");
        age.text = PlayerPrefs.GetString("age", "");
        sex.text = PlayerPrefs.GetString("sex", "");
        diag.text = PlayerPrefs.GetString("diag", "");
        lam.text = PlayerPrefs.GetString("lam", "");
        lan.text = PlayerPrefs.GetString("lan", "");
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
            SceneManager.LoadScene("ARscene");
        }
    }
}
