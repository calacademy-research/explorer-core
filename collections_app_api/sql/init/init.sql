-- Create the configuration table to dynamically set model_url if it doesn't exist
CREATE TABLE IF NOT EXISTS app_config (
    config_key VARCHAR(255) PRIMARY KEY,
    config_value VARCHAR(255)
);

-- Insert the bind address (adjust as needed)
-- You can also make this dynamic if desired
INSERT INTO app_config (config_key, config_value)
VALUES ('bind_address', '0.0.0.0')
ON DUPLICATE KEY UPDATE config_value = '0.0.0.0';  -- Update if already exists
