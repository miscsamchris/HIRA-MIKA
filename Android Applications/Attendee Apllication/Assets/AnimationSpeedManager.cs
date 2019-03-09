using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AnimationSpeedManager : MonoBehaviour {

    public Animator m_Animator;
    public TMPro.TMP_Text t;
	void Update () {
        m_Animator.speed = Time.deltaTime * float.Parse(t.text) * 0.7f;
    }
}
