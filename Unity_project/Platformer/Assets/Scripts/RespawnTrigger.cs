using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(EdgeCollider2D))]

public class RespawnTrigger : MonoBehaviour {

	/// <summary>
	/// Start is called on the frame when a script is enabled just before
	/// any of the Update methods is called the first time.
	/// </summary>
	void Start()
	{
		GetComponent<EdgeCollider2D>().isTrigger = true;
	}

	/// <sumary>
	/// Sent when another object enters a trigger collider attached to this
	/// object (2D physics only)
	/// </summary>
	/// <param name="other">The Collider2D involved in this collision.</param>
	void OnTriggerEnter2D(Collider2D other)
	{
		// Debug
		if(!other.CompareTag("Player"))
		{
			return;
		} else
		{
			Debug.Log("Player collided with killing object.");
		}

		Respawn pr = other.GetComponent<Respawn>();
		if(!pr)
			return;

		pr.playerRespawn();
	}
}
