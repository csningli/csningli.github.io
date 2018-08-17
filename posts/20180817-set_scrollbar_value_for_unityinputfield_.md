# Set Scrollbar's Value for Unity InputField

When the InputField is associated with a Scrollbar, the position of the bar can be changed via setting its value attribute.

However, if you change scrollbar's value (in the script) right after the inputfield's content changed, usually it won't work as expected. The reason is simple. If the change of the scrollbar's value happen in the same Update() scope with the change of content, then the content area has not been updated correctly and hence the bar only change according to the old content.

The solution is also simple. If you want to scroll the bar according to the latest content, then you should change scrollbar's value in the next (or even later) Update() scope.

    public Scrollbar scrollbar;
    private bool contentChanged = false;

    void Update ()
    {
        if (contentChanged)
        {
            scrollbar.value = 1f; // always scroll to the bottom; change to 0f to scorll to the top
            contentChanged = false;
        }

        // update the content

        if (Changed(content))
        {
            contentChanged = true;
        }
    }

    private bool Changed (Text content)
    {
        // return true if 'content' has changed; otherwise return false
    }

Just for comment, someone suggests doing "Canvas.ForceUpdateCanvases()". However, this doesn't always work.
