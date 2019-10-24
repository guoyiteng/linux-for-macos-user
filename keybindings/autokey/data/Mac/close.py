store.set_global_value('hotkey', '<meta>+w')
if re.match('.*(Hyper)', window.get_active_class()):
    logging.debug('terminal')
    engine.set_return_value('<ctrl>+<shift>+w')
else:
    logging.debug('normal')
    engine.set_return_value('<ctrl>+<f4>')
engine.run_script('combo')