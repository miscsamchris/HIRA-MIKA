using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AnimationSpeedManager : MonoBehaviour {

    public Animator m_Animator;
    public float speed;
	void Update () {
        m_Animator.speed = Time.deltaTime * speed;
    }
}
