using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class Player : MonoBehaviour
{
    public float speed = 3f;
    public float jumpForce = 10f;
    public bool isDead;
    public bool levelFinished;
    public bool canControl;

    private Rigidbody2D rb;
    private SpriteRenderer sRend;
    private Animator anim;
    //Use this for intilization
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        sRend = GetComponent<SpriteRenderer>();
        anim = GetComponent<Animator>();

        canControl = true;
        isDead = false;
        levelFinished = false;
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        float ySpeed = rb.velocity.y;

        if (canControl)
        {

        	// Movement 
        	if (Input.GetKey(KeyCode.A))
        	{
        	    rb.velocity = new Vector2(-speed, ySpeed);
        	    sRend.flipX = true;
        	    anim.SetBool("Moving", true);
        	}
        	else if (Input.GetKey(KeyCode.D))
        	{
        	    rb.velocity = new Vector2(speed, ySpeed);
        	    sRend.flipX = false;
        	    anim.SetBool("Moving", true);
        	}
        	// If landed & not moving
        	else if (!Input.GetKey(KeyCode.A) && !Input.GetKey(KeyCode.D) && Mathf.Approximately(ySpeed,0f))
        	{
        	    rb.velocity = Vector2.zero;
        	    anim.SetBool("Moving", false);
        	}
        	// Jump
        	if (Input.GetKeyDown(KeyCode.Space) && Mathf.Approximately(ySpeed, 0f))
        	{
        		rb.velocity = new Vector2(rb.velocity.x, jumpForce);
        		anim.SetBool("Jumping", true);
        	}
        	// Checking if falling
        	if(rb.velocity.y < 0f)
        	{
        		anim.SetBool("Jumping", false);
        		anim.SetBool("Falling", true);
        	}
        	else
        	{
        		anim.SetBool("Falling", false);
        	}
    	}
    }

    void OnTriggerEnter2D(Collider2D other)
    {
    	if (other.gameObject.tag == "Enemy") // If player hits the spikes
    	{
    		canControl = false;
    		anim.SetBool("Death", true);
            isDead = true;
    	}
    	if (other.gameObject.tag == "Finish") // If player hits the goal
    	{
    		canControl = false;
    		anim.SetBool("Moving", false);
            levelFinished = true;
    	}
    }
}
