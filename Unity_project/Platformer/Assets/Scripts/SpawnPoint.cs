using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(BoxCollider2D))]

public class SpawnPoint : MonoBehaviour {

	/// <summary>
	/// Awake is called when the script instance is being loaded.
	/// </summary>
	void Awake()
	{
		GetComponent<BoxCollider2D>().isTrigger = true;
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
			Debug.Log("Player collided with SpawnPoint.");
		}
		
		Respawn pr = other.GetComponent<Respawn>();
		if(!pr)
			return;

		// saving position
		pr.spawn = transform;
	}
}
