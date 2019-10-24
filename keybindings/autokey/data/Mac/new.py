store.set_global_value('hotkey', '<meta>+n')
if re.match('.*(Hyper)', window.get_active_class()):
    logging.debug('terminal')
    engine.set_return_value('<ctrl>+<shift>+n')
else:
    logging.debug('normal')
    engine.set_return_value('<ctrl>+n')
engine.run_script('combo')